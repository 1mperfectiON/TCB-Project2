from dhooks import Webhook,Embed
from datetime import date,datetime

def SendOutWebhook():
    embed=Embed(
    title="KITH MOSAIC TEE/SLATE(并没有补货)",
    url="https://kith.com/collections/kith-monday-program/products/kith-mosaic-tee-slate",
    description="In Stock Now!",
    color=6940159,
    timestamp="now",
    )


    hook=Webhook("https://ptb.discordapp.com/api/webhooks/665206935125098496/5nqd6ABS3So5UVCRle7nZIqhJ8wRLFPCBbTReW9MqC6l8A9zYiUe4TlRCwbTMtn0Ov_u")

    embed.add_field(name="商品页面",value="https://cdn.shopify.com/s/files/1/0094/2252/products/KH3777-105-2_300x300.jpg?v=1590786070")
    embed.set_author(name="eee7272的小小monitor",icon_url="https://cdn.discordapp.com/avatars/677904239527329817/a5fb74580580dd6d3354e8ecd7f136ee.png?size=128")
    embed.set_image("https://cdn.shopify.com/s/files/1/0094/2252/products/KH3777-105_200x200_crop_center.jpg?v=1590786070")
    embed.set_footer(text="eee7272#6012",icon_url="https://cdn.discordapp.com/avatars/677904239527329817/a5fb74580580dd6d3354e8ecd7f136ee.png?size=128")

    hook.send(embed=embed)
