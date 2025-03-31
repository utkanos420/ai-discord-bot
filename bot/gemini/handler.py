from openai import OpenAI
import os
from imgur.dowloader import upload_image_to_imgur
from configs.config import client

async def handle_attachments_and_request(ctx, message):
    save_dir = "temp"
    os.makedirs(save_dir, exist_ok=True)

    await ctx.send("Запрос получен!")

    for attach in ctx.message.attachments:
        file_path = os.path.join(save_dir, attach.filename)
        await attach.save(file_path)

        try:
            imgur_link = upload_image_to_imgur(file_path)
            prompt = message

            completion = client.chat.completions.create(
                extra_headers={
                    "HTTP-Referer": "<YOUR_SITE_URL>",
                    "X-Title": "<YOUR_SITE_NAME>",
                },
                model="google/gemini-2.5-pro-exp-03-25:free",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": prompt
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": imgur_link
                                }
                            }
                        ]
                    }
                ]
            )

            result = completion.choices[0].message.content

            while len(result) > 2000:
                await ctx.send(result[:2000])
                result = result[2000:]

            await ctx.send(result)

        except Exception as e:
            await ctx.send(f"Error: {e}")


async def handle_text_request(ctx, message):
    try:

        await ctx.send("Запрос получен!")

        prompt = message

        completion = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "<YOUR_SITE_URL>",
                "X-Title": "<YOUR_SITE_NAME>",
            },
            model="google/gemini-2.5-pro-exp-03-25:free",
            messages=[
                {
                    "role": "user",
                    "content": [{"type": "text", "text": prompt}]
                }
            ]
        )

        if not completion.choices or not completion.choices[0].message or not completion.choices[0].message.content:
            await ctx.send("Ошибка: ответ от API пуст или недоступен.")
            return

        result = completion.choices[0].message.content

        while len(result) > 2000:
            await ctx.send(result[:2000])
            result = result[2000:]

        await ctx.send(result)

    except Exception as e:
        await ctx.send(f"Error: {e}")
