from config import Config 
from faker import Faker
from telethon.tl.functions.messages import ImportChatInviteRequest
from pyrogram import Client, filters
from pyrogram.types import Message

APP_ID = Config.APP_ID
API_HASH = Config.API_HASH
SESSION = "1AZWarzQBu30fdAd7LNOqrflKl6zHlN6SHLo438OEs4Ed40hlDLdrdooeCkDC-szsSrLpJaSbxp06ILQJww-7C4qCl4H7uhHtfrX8peZK3_mpqKkMyz4FFYatz01zTogN3fLJyL1gF1SRyd_xG-nSl8AMuX_JMtGTERyUbPXjJZ8jExob7u-4XmtJbB7MEmKLXUL9nWb8Dab0j_j-O194OnXhsT6iUZPYdAKyhSuje-dZi8h3W3SluuhenSqxaomZvR-9LgEBvPT5M8C9pD9UnY8IzflVLq1OAOFtFGlEKDCyL7hTIQefDMJR5_z0DzhKGP42nkc3KP1GPssvLgBdrhXPHM9xjrE="

app = Client(
  StringSession(SESSION),
  (APP_ID),
  (API_HASH),
)EN,
)
bot_status = True

def generate_fake_info():
    fake = Faker()
    name = fake.name()
    street = fake.street_address()
    city = fake.city()
    state = fake.state()
    zip_code = fake.zipcode()
    phone = fake.phone_number()
    email = fake.email()
    password = fake.password()
    return f"Name: `{name}`\nStreet: `{street}`\nCity/Town: `{city}`\nState/Province/Region: `{state}`\nZip Code: `{zip_code}`\nPhone: `{phone}`\nEmail: `{email}`\nPassword: `{password}`"

@app.on_message(filters.command("fake"))
async def fake(_: Client, message: Message):
 if bot_status == False: await message.reply("- The bot is stopped, Try again later .")
 else:
  result = generate_fake_info()
  await message.reply(result)
  