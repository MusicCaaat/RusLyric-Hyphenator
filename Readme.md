# РуСлог / RusLyric Hyphenator

Профессиональная утилита для автоматической подготовки русского вокального текста к вставке в нотные редакторы (**Sibelius, Finale).

### О программе
В нотаторах Сибелиус и Финал нет деления на слоги русских слов. Для вставки в ноты слогов на русском приходится самому делить слова на слоги, либо обращаться к специальным сервисам или нейросетям. Любой из этих способов неудобный и затратный по времени. Также, после самостоятельного деления на слоги возникают другие проблемы при вставке их в ноты – при наличии в тексте предлогов «в», «к», «с», а также частиц «ж», «ль», «б» нотатор, после вставки этих предлогов или частиц, автоматически перебрасывает на следующую ноту. Это заставляет возвращаться к предлогу/частице и использовать неразрывный пробел (ещё одно лишнее действие).

**РуСлог** автоматизирует процесс подготовки текста, избавляя от ручной расстановки дефисов и неразрывных пробелов между предлогами и слогами/словами и между словами/слогами и частицами.

### Основные функции:
* **Вокальный слогораздел:** Алгоритм делит слова на слоги, стремясь к "открытым" слогам (оканчивающимся на гласную), что соответствует правилам вокального исполнения.
* **Умная привязка предлогов:** Автоматически объединяет предлоги `в, к, с` со следующим словом через неразрывный пробел. Предлог всегда остается вместе со словом на одной ноте.
* **Работа с частицами:** Частицы `ж, б, ль` привязываются к предыдущему слову/слогу.

### Инструкция по применению:
1.	Скопируйте исходный русский текст из любого источника (Word, блокнот, браузер).
2.	Запустите файл `RusLyric_Hyphenator.exe` (ни консоли, ни отображения окна с программой не будет, всё произойдёт в фоновом режиме – отредактированный текст сразу окажется в буфере обмена).
3. Перейдите в нотный редактор, выберите первую ноту и активируйте инструмент ввода текста (Lyrics).
4. Нажимайте `Ctrl+V`. Программа сама расставит слоги по нотам.

Чего НЕ удалось достичь – правильного копирования в ноты начала прямой речи. Т.е. текст типа “«- Деление слов…»” (прямая речь с кавычками) нотатор будет менять на « - Деление слов», а “- Деление слов” (т.е. прямая речь без кавычек), нотатор будет менять на “Деление слов”. Дефис/тире в начале текста он будет игнорировать сразу, «приклеенный» к кавычке дефис/тире он будет разделять пробелом. 
Также была идея создания программы, чтобы она работала в трее. Т.е. после запуска любой скопированный текст сразу делится на слоги и возвращается в буфер обмена. НО такой способ не смог устранить проблему сочетания предлога «в» со словами/слогами начинающимися на «т». Почему в такой версии программы неразрывный пробел (неважно в каком из 3х вариантов) не срабатывает и, например, сочетание «в том» отображается как «втом», что заставляет вернуться к этой ноте и вручную вбивать неразрывный пробел между предлогом и словом/слогом. 

Для разработчиков: Если вы хотите изменить логику слогоделения под свои задачи (например, использовать строгий школьный перенос), вы можете отредактировать соответствующие правила в исходном коде (RusLyric_Hyphenator.py) в секции обработки согласных.

---

### Поддержать проект
Если программа сэкономила вам время и вы хотите поблагодарить автора, вы можете отправить донат на развитие проекта через **ЮMoney**:
* **[Поддержать автора (картой или из кошелька)](https://yoomoney.ru/to/4100118714515464)**


English Version
RusLyric Hyphenator / RuSlog

A professional utility for automatic processing of Russian vocal texts for music notation software (Sibelius, Finale).
About the Program

Music notation programs like Sibelius and Finale do not support automatic hyphenation for the Russian language. Users are forced to manually split lyrics into syllables or use external services, which is time-consuming.

Furthermore, manual hyphenation often causes issues with Russian prepositions ("в", "к", "с") and particles ("ж", "ль", "б"). By default, notation software moves to the next note after these characters, forcing the user to manually insert non-breaking spaces every single time.

RusLyric Hyphenator automates this process by handling both hyphenation and the insertion of non-breaking spaces between prepositions, syllables, and particles.
Key Features:

    Vocal Hyphenation: The algorithm follows classical vocal rules, favoring "open" syllables (ending in a vowel). For example, "кар-та" becomes "ка-рта", which is the standard for professional singing.

    Smart Preposition Binding: Automatically binds prepositions в, к, с to the following word using a non-breaking space. This ensures the preposition stays on the same note as the word.

    Particle Binding: Particles ж, б, ль are automatically bound to the preceding syllable/word.

How to Use:

    Copy your Russian source text from any document (Word, Notepad, Browser).

    Run RusLyric_Hyphenator.exe. (The program runs silently in the background; there is no window. Your clipboard will be updated instantly).

    Switch to your notation software, select the first note, and activate the Lyrics tool.

    Press Ctrl+V. The program will automatically distribute the syllables across the notes.

Known Limitations:

Currently, the program has issues with direct speech formatting at the beginning of a line (quotation marks and dashes). Notation software may incorrectly interpret or strip dashes when they are attached to quotation marks.

The "Always-in-Tray" background mode was considered but discarded due to specific technical conflicts (e.g., the "в том" issue where non-breaking spaces failed in certain combinations, causing words to merge). The current "run-on-demand" approach remains the most reliable.

For Developers: If you wish to modify the hyphenation logic (e.g., to use strict academic/school rules), you can edit the consonant processing rules in the source code (RusLyric_Hyphenator.py).

---

### Support the Project
If you find this tool useful and would like to support the developer, you can make a donation via **Yoomoney** (supports bank cards):
* **[Donate via Yoomoney](https://yoomoney.ru/to/4100118714515464)**



