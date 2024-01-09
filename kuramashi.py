import streamlit as st  # Streamlitをインポート
import pandas as pd  # pandasをインポート

def main():
    st.title('倉増アプリ')  # アプリのタイトル

    # Excelファイルのアップロード部分
    st.subheader('二つのExcelファイルをアップロードしてください')
    file1 = st.file_uploader('一つ目のExcelファイルをアップロード', type=['xlsx'])
    file2 = st.file_uploader('二つ目のExcelファイルをアップロード', type=['xlsx'])

    # 両方のファイルがアップロードされた場合の処理
    if file1 and file2:
        # アップロードされたファイルからシート名を取得
        sheets_file1 = pd.ExcelFile(file1).sheet_names
        sheets_file2 = pd.ExcelFile(file2).sheet_names

        # シートを選択するためのプルダウンメニュー
        st.subheader('各ファイルからシートを選択してください')
        selected_sheet1 = st.selectbox('一つ目のファイルからシートを選択', sheets_file1)
        selected_sheet2 = st.selectbox('二つ目のファイルからシートを選択', sheets_file2)

        # 情報転記を実行するボタン
        if st.button('情報転記を実行'):
            st.write('情報転記を開始します...')

            # 選択されたシートを読み込み
            df1 = pd.read_excel(file1, sheet_name=selected_sheet1)
            df2 = pd.read_excel(file2, sheet_name=selected_sheet2)

            # ここで、シート間の情報転記のロジックを追加
            # 例: df1とdf2のデータを比較、結合、またはコピー
            #     必要なデータ処理を行い
            #     結果を画面に表示または新しいExcelファイルとして保存

            st.write('情報転記が完了しました！')

# アプリを実行
if __name__ == "__main__":
    main()
