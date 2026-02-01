import pyperclip
import re

def is_russian(text):
    return bool(re.search('[а-яёА-ЯЁ]', text))

def syllabify_word(word):
    if not is_russian(word):
        return word

    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    sonorants = "рлмнРЛМН"
    
    vowel_indices = [i for i, char in enumerate(word) if char in vowels]
    
    if len(vowel_indices) <= 1:
        return word

    syllables = []
    start = 0
    
    for i in range(len(vowel_indices) - 1):
        v1 = vowel_indices[i]
        v2 = vowel_indices[i+1]
        between = word[v1+1 : v2]
        split_offset = 0 
        
        if not between:
            split_offset = 0
        elif "ться" in between.lower():
            idx = between.lower().find("ться")
            split_offset = idx
        elif "тся" in between.lower():
            idx = between.lower().find("тся")
            split_offset = idx
        elif "зж" in between.lower():
            idx = between.lower().find("зж")
            split_offset = idx
        else:
            curr_split = 0 
            for j, char in enumerate(between):
                if char.lower() in "йьъ":
                    curr_split = j + 1
                elif char in sonorants:
                    if j + 1 < len(between):
                        next_char = between[j+1]
                        if next_char.lower() not in "ьъ" and next_char not in sonorants:
                            curr_split = j + 1
            split_offset = curr_split

        split_index = v1 + 1 + split_offset
        syllables.append(word[start:split_index])
        start = split_index

    syllables.append(word[start:])
    return "-".join(syllables)

def process_text(text):
    # 1. Схлопываем лишние пробелы
    text = re.sub(r' +', ' ', text)

    # 2. Делим на токены и слоги
    tokens = re.split(r'([а-яёА-ЯЁa-zA-Z]+)', text)
    processed = [syllabify_word(t) if is_russian(t) else t for t in tokens]
    result = "".join(processed)
    
    # 3. NBSP для предлогов (В, К, С) — привязка СПРАВА
    pattern_prep = r'(?i)\b(в|к|с) +([а-яёА-ЯЁa-zA-Z\-]+)'
    def prep_replacer(match):
        prep, word = match.group(1), match.group(2)
        return f"{prep}\u00A0{word}"
    
    result = re.sub(pattern_prep, prep_replacer, result)

    # 4. NBSP ТОЛЬКО для кратких частиц (ж, б, ль) — привязка СЛЕВА
    # Убрал "же", "бы", "ли".
    pattern_part = r'(?i)([а-яёА-ЯЁ\-]+) +(ж|б|ль)\b'
    
    def part_replacer(match):
        word_part, particle = match.group(1), match.group(2)
        return f"{word_part}\u00A0{particle}"

    result = re.sub(pattern_part, part_replacer, result)
    
    return result

if __name__ == "__main__":
    try:
        clipboard_text = pyperclip.paste()
        if not clipboard_text or not clipboard_text.strip():
            print("Буфер пустой. Скопируй текст и запусти снова.")
        else:
            # Очистка результата перед выдачей
            final_text = process_text(clipboard_text)
            pyperclip.copy(final_text)
            print(f"Готово! Обработано.")
            print(f"Результат: {final_text[:100]}...")
            
    except Exception as e:
        print(f"Ошибка: {e}")