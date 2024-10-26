import requests

def generate_qr(url):
    # URLをエンコード
    api_url = f"https://qr-make-api.onrender.com/qr/{requests.utils.quote(url)}"
    response = requests.get(api_url)

    if response.status_code == 200:
        print("QRコードが正常に生成されました。")
        # レスポンスの内容をファイルとして保存
        with open("qr.png", "wb") as f:
            f.write(response.content)
        print("QRコード画像が 'qr.png' として保存されました。")
    else:
        print("QRコードの生成に失敗しました。")
        print("ステータスコード:", response.status_code)
        print("レスポンス:", response.text)

# 使用例
generate_qr("https://qr-make-api.onrender.com")
