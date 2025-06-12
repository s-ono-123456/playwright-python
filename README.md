# Googleスクリーンショットツール

このプロジェクトは、[Playwright](https://playwright.dev/python/)を使用してGoogleのトップページのスクリーンショットを自動で取得するPythonスクリプトです。

## 構成ファイル

- `google_screenshot.py` : Googleのトップページを開き、スクリーンショットを保存するメインスクリプト
- `requirements.txt` : 必要なPythonパッケージ（Playwright）
- `google_screenshot.spec` : PyInstaller用の設定ファイル
- `build/` : PyInstallerによるビルド成果物

## 必要条件

- Python 3.7以上
- pip

## セットアップ方法

1. 依存パッケージのインストール

```powershell
pip install -r requirements.txt
```

2. Playwrightのブラウザバイナリをインストール

```powershell
python -m playwright install
```

## 使い方

```powershell
python google_screenshot.py
```

実行後、`screenshots`フォルダ内に`google.png`というファイル名でスクリーンショットが保存されます。

## ビルド方法（PyInstallerを利用する場合）

PyInstallerをインストールしていない場合は、以下でインストールしてください。

```powershell
pip install pyinstaller
```

ビルドコマンド例：

```powershell
$env:PLAYWRIGHT_BROWSERS_PATH="0"
playwright install chromium
pyinstaller google_screenshot.spec
```

## ライセンス

このリポジトリはMITライセンスです。

---

> 本READMEは自動生成されました。
