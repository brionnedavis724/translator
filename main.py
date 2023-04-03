from translate import Translator
translator = Translator(to_lang='ja')
# translation = translator.translate("This is a pen.")

try:
    with open('./test.txt', mode='r') as my_file:
        # print(my_file.read())
        text = my_file.read()
        translation = translator.translate("This is a pen.")
        translation2 = translator.translate(text)
        translation3 = translator.translate('commit new changes in pycharm')
        print(translation)
        print(translation2)
except FileNotFoundError as e:
    print('check your file path')