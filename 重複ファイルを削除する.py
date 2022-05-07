import hashlib
import glob
import shutil

# 以下のディレクトを作成する。
mv_dir = "_duplicate"

if __name__ == "__main__":
    # ファイルのリストを作成（拡張子で判断）
    file_list = glob.glob("./**/*.mp4", recursive=True)
    output = {}
    print("%sファイルが見つかりました。" % len(file_list))
    for fname in file_list:
        # 以下のディレクトリは除外
        if not("重複データ" in fname) and not(mv_dir in fname):
            with open(fname, 'rb') as file:
                fileData = file.read()
            hash_sha1 = hashlib.sha1(fileData).hexdigest()
            if not(hash_sha1 in output):
                output[hash_sha1] = []
            else:
                print("重複データが見つかりました。移動します。（%s）" % file.name)
                try:
                    shutil.move(file.name, mv_dir + "/")
                except Exception as e:
                    print("移動中にエラーが発生しました。")
                    print(e)
            output[hash_sha1].append(file.name)
    print(output)
