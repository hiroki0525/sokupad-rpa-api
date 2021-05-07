# sokupad-rpa-api（β版）
即パッドを通じてRPAで馬券を購入するAPIです。

## 開発環境構築
1. poetryの導入
```shell
# インストール&有効化
curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
source $HOME/.poetry/env

# ローカルプロジェクトにvenv
poetry config virtualenvs.in-project true
```

2. 依存パッケージ導入

`poetry install`

## ローカルサーバーの起動
`poetry run uvicorn server:app --reload`

## API仕様書
http://127.0.0.1:8000/docs

## テスト
コマンド

`pytest`

## 注意事項
* [即パッド利用規約](https://www.jra.go.jp/dento/member/soku/yakujo_soku.pdf) やサーバー側の負荷、マナーなどを考慮してください。
* Apache Licenseに則り、当プログラムから生じたいかなる損害についても一切責任は負いません。

## License
Apache License 2.0