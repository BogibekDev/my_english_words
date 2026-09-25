# my_english_words

Otaxonjonning "vocab_game" ilovasi uchun so'zlar va audiolar.

**Repo private bo'lib qolishi kerak.** Audiolar Cambridge Dictionary'dan olingan va faqat shaxsiy foydalanish uchun.

## Tuzilishi

```
lessons/unit1.json   har bir dars alohida faylda
audio/uk/<so'z>.mp3  britancha talaffuz
audio/us/<so'z>.mp3  amerikacha talaffuz
tools/fetch_audio.py yetishmayotgan audiolarni yuklab oladi
```

## Dars fayli

`lessons/unit2.json`:

```json
{
  "title": "2-dars: Ranglar",
  "words": [
    { "en": "red", "uz": "qizil", "emoji": "🟥" },
    { "en": "blue", "uz": "ko'k", "emoji": "🟦" }
  ]
}
```

- Fayl nomi darsning identifikatori hisoblanadi. Bolaning progressi fayl nomiga bog'langani uchun, fayl yaratilgandan keyin uning nomini o'zgartirmang.
- Ilovada darslar fayl nomi bo'yicha tartiblanadi: `unit1`, `unit2`, ..., `unit10`.
- `en` va `uz` maydonlari majburiy. `emoji` ixtiyoriy: agar bo'lmasa, ilova o'zbekcha tarjimani katta harflar bilan ko'rsatadi.
- `audio` maydonini qo'lda yozish shart emas.

## Audio qo'shish

```sh
python3 tools/fetch_audio.py
git add -A && git commit -m "Add unit2" && git push
```

Audiosi topilmagan so'zlar uchun ilova qurilmaning o'z ovozidan (TTS) foydalanadi.

O'zgarishlar ilovadagi **"Yangilash"** tugmasi bosilganda yuklab olinadi.
