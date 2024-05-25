import pandas

pandas_df_dict = pandas.read_excel("angle_map.xlsx", [0, 1, 2])
print(pandas_df_dict[1])
print(pandas_df_dict[1].interpolate(method="polynomial", order=5))

# line = str("")
# line.find()
# while line.find("Ready for input")>-1:
#     pass

