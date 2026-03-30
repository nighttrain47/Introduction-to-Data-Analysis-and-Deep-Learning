# -*- coding: utf-8 -*-
"""
CÂU 4: XỬ LÝ DỮ LIỆU THIẾU CHO CỘT DÂN TỘC (DT)
"""

import pandas as pd

df = pd.read_csv(r"DuLieu\dulieuxettuyendaihoc.csv")

print("Số giá trị thiếu trong cột DT:", df["DT"].isna().sum())

df["DT"] = df["DT"].fillna(0)

print("Số giá trị thiếu sau khi xử lý:", df["DT"].isna().sum())

df.to_csv(r"DuLieu\data_da_sua.csv", index=False)
print("Đã lưu file: DuLieu\\data_da_sua.csv")
