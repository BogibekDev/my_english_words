# my_english_words

Otaxonjonning "vocab_game" ilovasi uchun so'zlar va audiolar.

**Repo private bo'lib qolishi kerak.** Audiolar Cambridge Dictionary'dan olingan va faqat shaxsiy foydalanish uchun.

## Tuzilishi

```
lessons.json        barcha darslar va so'zlar
audio/uk/<so'z>.mp3 britancha talaffuz
audio/us/<so'z>.mp3 amerikacha talaffuz
tools/fetch_audio.py yetishmayotgan audiolarni yuklab oladi
```

## So'z qo'shish

`lessons.json` faylida kerakli darsning `words` ro'yxatiga yangi qator qo'shing:

```json
{ "en": "bird", "uz": "qush", "emoji": "🐦" }
```

Yangi dars qo'shish uchun `lessons` ro'yxatiga yangi element qo'shing:

```json
{
  "id": "unit2",
  "title": "2-dars: Ranglar",
  "words": [
    { "en": "red", "uz": "qizil", "emoji": "🟥" }
  ]
}
```

- `en` va `uz` majburiy. `emoji` ixtiyoriy: bo'lmasa, ilova o'zbekcha tarjimani katta harf bilan ko'rsatadi.
- `id` har bir dars uchun boshqacha bo'lishi va keyin o'zgarmasligi kerak, chunki bolaning progressi shu `id` ga bog'langan.
- `audio` maydonini qo'lda yozish shart emas.

Keyin audiolarni qo'shish uchun:

```sh
python3 tools/fetch_audio.py
git add -A && git commit -m "Add words" && git push
```

Audiosi yo'q so'zlar uchun ilova qurilmaning ovozidan (TTS) foydalanadi.

Ilovada **"Yangilash"** tugmasi bosilganda o'zgarishlar yuklab olinadi.
