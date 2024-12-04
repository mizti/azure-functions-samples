# Azure Functionサンプルデプロイ集

## Python (プログラミングモデルv2)

* ディレクトリ: python_v2

### デプロイ方法

##### zipによるデプロイ
```shell
cd python_v2
zip ../function.zip *
cd ..
az functionapp deployment source config-zip \
    --resource-group $RESOURCE_GROUP \
    --name $FUNCTION_APP_NAME \
    --src  function.zip
```
zip化するときに、python_v2自体のフォルダを含まないように注意。

----


----


----

## そのほか重要なコマンド

#### 関数アプリ内の関数を一覧する
```shell
az functionapp function list --resource-group $RESOURCE_GROUP --name $FUNCTION_APP_NAME
```
