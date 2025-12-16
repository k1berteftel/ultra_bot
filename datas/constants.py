

prices = {
    'image': {
        'text': 12,
        'combo': 41
    },
    'video': {
        'kling': 121,
        'seedance': {
            'lite': 61,
            'pro': 81
        },
        'sora': 61
    },
    'task': 11
}


duration_prices = {
    'seedance_lite': {
        5: 61,
        10: 101
    },
    'seendance_pro': {
        5: 81,
        10: 131,
    },
    'kling': {
        5: 121,
        10: 242,
    },
    'sora': {
        5: 61,
        10: 71,
        15: 81
    }
}

model_ratios = {
    'seedance': ["16:9", "9:16"],
    'kling': ["16:9", "9:16"],
    'sora': ["16:9", "9:16"]
}


model_examples = {
    'image': {
        'text': {
            'text': '<b>Промпт:</b>\n<blockquote expandable>Летающий остров в форме черепахи с замком на спине, '
                    'парящий в фиолетовом небе</blockquote>',
            'media': 'media/image_gen/text_img.jpg',
            'media_type': 'photo',
            'url': 'https://t.me/flex_generate'
        },
        'combo': {
            'text': '<b>Промпт:</b>\n<blockquote expandable>Make a vertical 3-frame low-res webcam collage using my '
                    'face. Warm dim screen lighting, grainy/noisy Photo Booth vibe, simple warm bedroom background.'
                    '\nExaggerated pout, finger near lip, pink camisole.\nShy/flirty tilt, soft expression, pink '
                    'hearts overlay.\nDramatic late-night pose, darker camisole, hand near mouth.\nUse my face '
                    'consistently.</blockquote>',
            'media': 'media/image_gen/text+photo_img.jpg',
            'media_type': 'photo',
            'url': 'https://t.me/flex_generate'
        },
    },
    'video':  {
        'kling': {
            'text': '<b>Промпт:</b>\n<blockquote expandable>The setting has warm lighting from streetlights or '
                    'soft party lights. A little boy around 2 to 3 years old, with light skin tone, broun hair, '
                    'and big green expressive eyes, runs joyfully toward a young couple sitting close together. '
                    'The couple must look exactly like the people in the attached photo — no changes to their facial '
                    'features, skin tone, hairstyle, or clothing. They both have medium skin, man have dark hair, '
                    'women have broun hair and are man wearing summer outfits. The child should clearly look like '
                    'the boy, with features that naturally combine both parents. He hugs them lovingly, wrapping her '
                    'arms around them, smiling and laughing. The couple smiles and embraces he warmly. The video '
                    'should feel authentic, as if casually filmed by a friend or family member on a phone — slightly '
                    'shaky, casually composed, and emotionally genuine</blockquote>',
            'media_type': 'video',
            'media': 'media/video_gen/kling.MP4',
            'url': 'https://t.me/flex_kling_generate'
        },
        'seedance': {
            'lite': {
                'text': '<b>Промпт:</b>\n<blockquote expandable>Пусть Этот человек моргнет, и улыбнется</blockquote>',
                'media': 'media/video_gen/seedance_video.mp4',
                'media_type': 'video',
                'url': 'https://t.me/flex_seedance_generate'
            },
            'pro': {
                'text': '<b>Промпт:</b>\n<blockquote expandable>Пусть Этот человек моргнет, и улыбнется</blockquote>',
                'media': 'media/video_gen/seedance_video.mp4',
                'media_type': 'video',
                'url': 'https://t.me/flex_seedance_generate'
            },
        },
        'sora': {
            'text': '<b>Промпт:</b>\n<blockquote expandable>Make a Boxer dog training in a gym against a '
                    'punching bag, the camera switches every 3 seconds, and you can hear the dog’s voice '
                    'motivating itself. He only has one glove on each hand.</blockquote>',
            'media_type': 'video',
            'media': 'media/video_gen/sora_ex.mp4',
            'url': 'https://t.me/flex_sora_generate'
        },
    }
}


def get_video_price(data: dict):
    model = data.get('model')
    sub_model = data.get('sub_model')
    params = data.get('params')
    model_name = model
    if model in ['seedance']:
        model_name = model + '_' + sub_model
    price = duration_prices[model_name].get(params.get('duration'))
    return price