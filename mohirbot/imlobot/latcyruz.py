from transliterate.base import TranslitLanguagePack, registry
from transliterate import translit

'''
pip install transliterate
'''
class UzbekLanguagePack(TranslitLanguagePack):
    language_code = "uz"
    language_name = "Uzbek"
    mapping = (
        u"abvgdjziyklmnsoprtufx'e",
        u"абвгджзийклмнсопртуфхъе"
    )
    pre_processor_mapping = {
    u"ch": u"ч",
    u"ye": u"е",
    u"g'": u"ғ",
    u"g‘": u"ғ",
    u"h": u"ҳ",
    u"q": u"қ",
    u"o'": u"ў",
    u"o‘": u"ў",
    u"sh": u"ш",
    u"ya": u"я",
    u"yo": u"ё",
    u"yu": u"ю",
    u"ts": u"ц",
   
    
  
    }
    reversed_specific_pre_processor_mapping = {
    u"ч": u"ch",
    u"э": u"e",
    u"е": u"ye",
    u"ғ": u"g'",
    u"ҳ": u"h",
    u"қ": u"q",
    u"ў": u"o'",
    u"ш": u"sh",
    u"я": u"ya",
    u"ё": u"yo",
    u"ю": u"yu",
    u"ю": u"yu",
    u"ц": u"ts",
    u"ь":u""


    }


registry.register(UzbekLanguagePack)


def toLatin(matn):
    matn = matn.lower()
    lotin = translit( matn, 'uz',reversed=True)
    return lotin

def toCyrillic(matn):
    matn = matn.lower()
    if "sh" in matn:
        matn = matn.replace("sh","ш")
    elif "ch" in matn:
        matn = matn.replace("ch","ч")
    elif matn[0]=="e":
        matn = list(matn)
        matn[0] = "э"
        matn = ''.join(matn)
    kirill = translit( matn, 'uz')
    return kirill

