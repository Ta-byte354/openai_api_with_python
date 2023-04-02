import openai
import configparser

class FileControll:


    #送信のテキストエリアの内容を自然言語処理サービスに送信する。
    def api_send_text(self, send_text):
        config = configparser.ConfigParser()
        config.read("apikey.config")
        api_key = config["api_key"]["OPEN_API_KEY"]

        prompt = send_text
        model = "davinci"
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
            api_key=api_key
        )

        return response.choices[0].text


    #保存ボタンを押下することでテキストファイルに受信内容を保存する。
    def save_text(self, recieve_text):
        pass


if __name__ == '__main__':
    MainGui()
