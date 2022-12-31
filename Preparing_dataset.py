import pandas as pd
from sklearn.preprocessing import LabelEncoder
import cv2
import os
from tqdm import *
import shutil as sh
import subprocess
from sklearn.model_selection import KFold


df = pd.read_csv("train/labels.csv")
df.LabelName.value_counts()

df['image_width'] = 0
df['image_height'] = 0

for img_name in df.ImageID.unique():
    img_shape = cv2.imread(f'train/images/{img_name}').shape
    h = img_shape[0]
    w = img_shape[1]

    df.loc[df.ImageID == img_name, 'image_width'] = w
    df.loc[df.ImageID == img_name, 'image_height'] = h

# Bounding Box Attributes
df['w'] = df.XMax - df.XMin
df['h'] = df.YMax - df.YMin
df['area'] = df.w * df.h

# Normalizing
df.w = df.w / df.image_width
df.h = df.h / df.image_height

df['x_center'] = df.XMin/df.image_width + (df.w/2)
df['y_center'] = df.YMin/df.image_height + (df.h/2)

le=LabelEncoder()
df['classes'] = le.fit_transform(df.LabelName)

df['path']=df.ImageID.apply(lambda x: "train/images/"+x)


# Function for making folders (YOLO FORMAT)

def prep_path(train_df,valid_df,fold):
    for name,mini in tqdm(train_df.groupby('ImageID')):
        path2save = f'train2017{fold}_fold/'

        if not os.path.exists('data/labels/'+path2save):
            os.makedirs('data/labels/'+path2save)

        with open('data/labels/'+path2save+name.replace('.jpg','')+".txt", 'w+') as f:
            row = mini[['classes','x_center','y_center','w','h']].astype(float).values
            row = row.astype(str)
            for j in range(len(row)):
                text = ' '.join(row[j])
                f.write(text)
                f.write("\n")
        if not os.path.exists('data/images/{}'.format(path2save)):
            os.makedirs('data/images/{}'.format(path2save))
        sh.copy(mini.path.values[0],'data/images/{}{}'.format(path2save,name))


    for name,mini in tqdm(valid_df.groupby('ImageID')):
        path2save = f'val2017{fold}_fold/'

        if not os.path.exists('data/labels/'+path2save):
                    os.makedirs('data/labels/'+path2save)

        with open('data/labels/'+path2save+name.replace('.jpg','')+".txt", 'w+') as f:
            row = mini[['classes','x_center','y_center','w','h']].astype(float).values
            row = row.astype(str)
            for j in range(len(row)):
                text = ' '.join(row[j])
                f.write(text)
                f.write("\n")
        if not os.path.exists('data/images/{}'.format(path2save)):
            os.makedirs('data/images/{}'.format(path2save))
        sh.copy(mini.path.values[0],'data/images/{}{}'.format(path2save,name))


    import yaml
    dic_data={"train": f"data/images/train2017{fold}_fold/",
                "val": f"data/images/val2017{fold}_fold/",
                "path": "../",
                "nc": 1,
                "names":['pothole'] }


    with open(f'wheat{fold}.yaml', 'w') as outfile:
        yaml.dump(dic_data, outfile, default_flow_style=False)

k = 5
kf = KFold(n_splits=k)
fold=1
image_paths_valid = pd.DataFrame(df.ImageID.unique())
for train_index, test_index in kf.split(image_paths_valid):
    print(fold)
    X_train, X_test = image_paths_valid.iloc[train_index], image_paths_valid.iloc[test_index]
    valid_ids = X_test[0].values
    train_df = df.loc[~df.ImageID.isin(valid_ids)]
    valid_df = df.loc[df.ImageID.isin(valid_ids)]
    train_df.shape,valid_df.shape
    prep_path(train_df,valid_df,fold)

    fold += 1