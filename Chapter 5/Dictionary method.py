Marks = {
    "Rohan":67,
    "Harry":98,
    "Tushar":100,
    "Ujjwal":97,
    "Mohit":38,
    "Arnav":58
}
print(Marks.items())
print(Marks.keys())
print(Marks.values())

Marks.update({"Tushar":99})
print(Marks.items())

print(Marks.get("Tushar"))   # If key doesn't exist it gives "None"
print(Marks["Tushar"])  # WE DOES NOT PREFER it as it gives an ERROR if key doesn't exist


Test_Dic = Marks.copy()
print(Test_Dic.items()) 

Test_Dic.pop("Ujjwal","Not Found")
print(Test_Dic.items())

Test_Dic.clear()  # it will clear our whole dictionary
print(Test_Dic.items())
