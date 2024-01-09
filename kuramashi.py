import streamlit as st
import pandas as pd

def main():
    st.title('Excel情報転記アプリ')

    # Excelファイルのアップロード部分
    st.subheader('二つのExcelファイルをアップロードしてください')
    file1 = st.file_uploader('一つ目のExcelファイルをアップロード', type=['xlsx'], key="file1")
    file2 = st.file_uploader('二つ目のExcelファイルをアップロード', type=['xlsx'], key="file2")

    # 両方のファイルがアップロードされた場合の処理
    if file1 and file2:
        # アップロードされたファイルからシート名を取得
        sheets_file1 = pd.ExcelFile(file1).sheet_names
        sheets_file2 = pd.ExcelFile(file2).sheet_names

        # シートを選択するためのプルダウンメニュー
        st.subheader('各ファイルからシートを選択してください')
        selected_sheet1 = st.selectbox('一つ目のファイルからシートを選択', sheets_file1, key="selected_sheet1")
        selected_sheet2 = st.selectbox('二つ目のファイルからシートを選択', sheets_file2, key="selected_sheet2")

        # シート選択後の処理
        if st.button('シート選択完了'):
            # 選択されたシートを読み込み（ヘッダー行を指定）
            df1 = pd.read_excel(file1, sheet_name=selected_sheet1, header=5)  # 6行目がヘッダー
            df2 = pd.read_excel(file2, sheet_name=selected_sheet2, header=0)  # 1行目がヘッダー

            # 2のシートのヘッダー名に対応する1のシートのヘッダーを選択
            st.subheader('2のシートのヘッダー名に対応する1のシートのヘッダーを選択してください')
            header_mappings = {}
            for col in df2.columns:
                options = list(df1.columns)
                selected_option = st.selectbox(f'2のシートのヘッダー "{col}" に対応する1のシートのヘッダーを選択:', options, key=col+"_header")
                header_mappings[col] = selected_option

            st.write('選択が完了しました。')
            # ここに転記のロジックを追加

            st.write('情報転記が完了しました！')

# アプリを実行
if __name__ == "__main__":
    main()
