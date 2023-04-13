from pyrogram import Client, filters
from pyrogram.errors import MessageNotModified
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup,CallbackQuery
from pyromod import listen
import asyncio
from telethon.sync import TelegramClient
import pickle
from telethon.tl.types import InputPeerChannel
from telethon.errors.rpcerrorlist import SlowModeWaitError,SessionPasswordNeededError,PhoneNumberInvalidError,PhoneCodeInvalidError
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, PhoneNumberBannedError, ChatAdminRequiredError
from telethon.tl.functions.messages import SendMessageRequest
from telethon.errors.rpcerrorlist import ChatWriteForbiddenError, UserBannedInChannelError, UserAlreadyParticipantError, FloodWaitError
from telethon.tl.functions.channels import InviteToChannelRequest
import sys
import time
import os
from telethon.tl.functions.messages import ImportChatInviteRequest, AddChatUserRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.types import UserStatusRecently

tokenm = "6253761142:AAEnH8kMz2-DPsTDMBWhuzitbY_oH_g-DPA"
azadtoken="6133292754:AAFGXs19GpvCCqOVEJPBqKkNdeAOb4mp7QY"
diyartoken="6056948266:AAFaJkLEVTHLwVzmMQh0SBEu0gV__mAGoms"
api_id = 2460981
api_hash = '95aadab8da821b7052d316706bb529f6'
isdevam=True
user_register_dict = {}
user_register_dict["data"] = {}
user_register_dict["data"]['name'] = "True"
app = Client("sgsgdsdg, sdapb_bot", api_id, api_hash, bot_token=azadtoken)






main_menu = InlineKeyboardMarkup([
    [InlineKeyboardButton("📝 Oto mesaj", callback_data="option1"),InlineKeyboardButton("🖼 Oto fotoğraf+mesaj", callback_data="foto")],
[InlineKeyboardButton("💣 Bombalama", callback_data="bomba")],

    [InlineKeyboardButton("⚙️ Ayarlar", callback_data="ayarlar")],
[InlineKeyboardButton("⭐️ Özellikler", callback_data="ozellik")],


])

# Güncellenmiş menü

numaramenu = InlineKeyboardMarkup([
     [InlineKeyboardButton("📞 Numaraları göster", callback_data="nogoster")],
    [InlineKeyboardButton("✏️ Numara Ekle", callback_data="add_number"),InlineKeyboardButton("🛑Numara sil", callback_data="nosil")],

    [InlineKeyboardButton("🔙 Geri", callback_data="ayarlardon")]
])
grupmenu = InlineKeyboardMarkup([
     [InlineKeyboardButton("📞 Grupları göster", callback_data="grupgoster")],
    [InlineKeyboardButton("✏️ Grup Ekle", callback_data="add_grup"),InlineKeyboardButton("🛑Grup sil", callback_data="grupsil")],

    [InlineKeyboardButton("🔙 Geri", callback_data="ayarlardon")]
])
ayarlar = InlineKeyboardMarkup([
    [InlineKeyboardButton("📞 Numara menü", callback_data="option2"),InlineKeyboardButton("📞 Grup menü", callback_data="grupmenu")],
    [InlineKeyboardButton("👁 Mesajı göster", callback_data="mesajgoster"),InlineKeyboardButton("📝 Mesajı düzenle", callback_data="mesajedit")],
[InlineKeyboardButton("🖼 Fotoğraf yükle", callback_data="upload_photo")],
    [InlineKeyboardButton("🔙 Geri", callback_data="anamenudon")],

])
iptal = InlineKeyboardMarkup([
    [InlineKeyboardButton("🛑 Durdur", callback_data="stop")],

])
islem = InlineKeyboardMarkup([
    [InlineKeyboardButton("Başlatılıyor...", callback_data="add_number")],

])
async def process_upload_photo(client, query):
    if query.photo:
        file_name = f"photo/photo.jpg"
        await app.download_media(message=query.photo, file_name=file_name)
        await app.send_message(query.chat.id, f"Oto Fotoğraf + mesaj için fotoğraf yüklendi")
        await app.send_message(query.chat.id, "⚙️ Ayarlar", reply_markup=ayarlar)

@app.on_message(filters.command(["restart"]))
async def restart(client, message):
    app.restart()

    # Yanıt olarak gönderilecek mesajı hazırla
    text = "Autograpth oto mesaj yazılımı"

    # Mesajı gönder, inline keyboard'ı yanıt olarak ekle
    await app.send_message(chat_id=message.chat.id, text=text, reply_markup=main_menu)
@app.on_message(filters.command(["start"]))
async def start(client, message):

    # Yanıt olarak gönderilecek mesajı hazırla
    text = "Autograpth oto mesaj yazılımı"

    # Mesajı gönder, inline keyboard'ı yanıt olarak ekle
    await app.send_message(chat_id=message.chat.id, text=text, reply_markup=main_menu)

@app.on_message()
async def on_message(client, message):
    await process_upload_photo(client, message)
@app.on_callback_query()
async def callback_query_handler(client, query: CallbackQuery):
  if query.message.chat.id == 5015560002:
    message=query.message


    # Veriye göre yanıt mesajını oluştur

    if query.data == "option2":

        await query.edit_message_reply_markup(reply_markup=numaramenu)
    elif query.data == "ayarlar":
        await client.delete_messages(message.chat.id, [message.id])
        await app.send_message(query.message.chat.id, "⚙️ Ayarlar", reply_markup=ayarlar)
    elif query.data == "upload_photo":
        await client.delete_messages(message.chat.id, [message.id])
        await app.send_message(query.message.chat.id, f"Oto fotoğraf + mesaj için fotoğraf bekleniyor...")

    elif query.data == "ozellik":
        await client.delete_messages(message.chat.id, [message.id])
        text="⭐️ Özellikler(v1.2)\n\nİstediğiniz süre içinde istediğiniz her mesaj gönderme isşlemini sizin için yapabilirim\n\nAynı zamanda fotoğraflı mesajda gönderebilirim\n\nİstediğin kadar hesap ekleyebilirsin"
        await app.send_message(query.message.chat.id, text, reply_markup=main_menu)
    elif query.data == "mesajgoster":
        await client.delete_messages(message.chat.id, [message.id])
        f = open("message.txt", "r",encoding='utf-8')
        denem=f.read()
        await app.send_message(query.message.chat.id, f"{denem}")
        await app.send_message(query.message.chat.id, "⚙️ Ayarlar", reply_markup=ayarlar)


    elif query.data == "mesajedit":
        await client.delete_messages(message.chat.id, [message.id])
        f=open("message.txt","w",encoding='utf-8')
        yazi=await query.message.chat.ask(f'Lütfen bir mesaj girin:')
        f.write(yazi.text)
        f.close()
        await yazi.request.edit_text(f"Mesaj kaydedildi.")
        await app.send_message(query.message.chat.id, "⚙️ Ayarlar", reply_markup=ayarlar)

    elif query.data == "grupsil":
        await client.delete_messages(message.chat.id, [message.id])

        accs = []
        f = open('gruplar.txt', 'rb')
        while True:
            try:
                accs.append(pickle.load(f))
            except EOFError:
                break
        f.close()
        if len(accs)==0:
            await app.send_message(query.message.chat.id, "Hata : Hiç grup eklemedin", reply_markup=grupmenu)
        else:
             i = 0
             text = " Gruplar \n----------------\n"
             for acc in accs:
                 text = text + f'{[i]} {acc[0]}\n'
                 i += 1
             index = await query.message.chat.ask(f'{text}\nSilmek istediğin grup indexini gir :')
             phone = str(accs[int(index.text)][0])
             del accs[int(index.text)]

             f = open('gruplar.txt', 'wb')
             for account in accs:
                 pickle.dump(account, f)
             await index.request.edit_text(f"Grup silindi.")
             await app.send_message(query.message.chat.id, "Grup menüsü", reply_markup=grupmenu)

             f.close()
    elif query.data == "nosil":
        await client.delete_messages(message.chat.id, [message.id])


        accs = []
        f = open('hesaplar.txt', 'rb')
        while True:
            try:
                accs.append(pickle.load(f))
            except EOFError:
                break
        f.close()
        i = 0
        text = " Numaralar \n----------------\n"
        for acc in accs:
            text=text+f'{[i]} {acc[0]}\n'
            i += 1
        index =await query.message.chat.ask(f'{text}\nSilmek istediğin numara indexini gir :')
        phone = str(accs[int(index.text)][0])
        session_file = phone + '.session'
        if os.name == 'nt':
            os.system(f'del sessions\\{session_file}')
        else:
            os.system(f'rm sessions/{session_file}')
        del accs[int(index.text)]
        f = open('hesaplar.txt', 'wb')
        for account in accs:
            pickle.dump(account, f)
        await index.request.edit_text(f"Hesap silindi.")
        await app.send_message(query.message.chat.id, "Numara menüsü", reply_markup=numaramenu)

        f.close()



    elif query.data == "grupgoster":
        await client.delete_messages(message.chat.id, [message.id])

        accs = []

        f = open('gruplar.txt', 'rb')
        while True:
            try:
                accs.append(pickle.load(f))
            except EOFError:
                break
        f.close()

        i = 0
        text = " Gruplar \n----------------\n"
        if len(accs)==0:
            text = "Hiç grup eklemedin"


        for z in accs:
            text = text + f'[{i}]{z[0]}\n'
            i += 1
        await app.send_message(query.message.chat.id, text, reply_markup=grupmenu)




    elif query.data == "nogoster":
        await client.delete_messages(message.chat.id, [message.id])

        accs = []

        f = open('hesaplar.txt', 'rb')
        while True:
            try:
                accs.append(pickle.load(f))
            except EOFError:
                break
        f.close()

        i = 0
        text=" Numaralar \n----------------\n"
        for z in accs:
            text=text+f'[{i}]{z[0]}\n'
            i += 1
        await app.send_message(query.message.chat.id,text,reply_markup=numaramenu)




    elif query.data == "anamenudon":
        await client.delete_messages(message.chat.id, [message.id])
        text="Autograph : Katılmış olduğun gruplara istediğin her mesajı gönderebilirim"
        await app.send_message(query.message.chat.id,text,reply_markup=main_menu)
    elif query.data == "ayarlardon":
        await client.delete_messages(message.chat.id, [message.id])
        text="Ayarlar"
        await app.send_message(query.message.chat.id,text,reply_markup=ayarlar)
    elif query.data == "stop":
        stop_event = asyncio.Event()
        stop_event.set()
        user_register_dict["data"]['name']="False"
        await app.send_message(chat_id=query.message.chat.id, text="Autograph", reply_markup=main_menu)



    elif query.data == "option1":

      await client.delete_messages(message.chat.id, [message.id])
      user_register_dict["data"]['name'] = "True"

      accounts = []
      f = open('hesaplar.txt', 'rb')
      while True:
          try:
              accounts.append(pickle.load(f))
          except EOFError:
              break
      if len(accounts) == 0:
          text = "Hata : Hiç hesap eklemedin"
          await app.send_message(query.message.chat.id, text, reply_markup=main_menu)

      else:
        await app.send_message(query.message.chat.id, "Engellenmiş hesaplar kontrol ediliyor..")
        for a in accounts:
            phn = a[0]

            clnt = TelegramClient(f'sessions/{phn}', 3910389, '86f861352f0ab76a251866059a6adbd6')
            await clnt.connect()
            banned = []
            if not await clnt.is_user_authorized():
                try:
                    await clnt.send_code_request(phn)

                except PhoneNumberBannedError:
                    await app.send_message(query.message.chat.id, f' {phn} Banlandı !')
                    banned.append(a)
            for z in banned:
                accounts.remove(z)
                await app.send_message(query.message.chat.id, "Engellenmiş hesaplar silindi...")
            time.sleep(1)
            clnt.disconnect()


        f = open('message.txt', 'r',encoding='utf-8')
        mesaj = f.read()
        accounts = []
        f = open('hesaplar.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(f))
            except EOFError:
                break

        index = 1
        bilgi = "none"
        hatabilgi = "Henüz hata yok"
        # tüm hesapları yükle (telefon numaraları)
        accounts = []

        f = open('hesaplar.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(f))
            except EOFError:
                break

        print(f' Toplam Hesaplarınız: ')
        number_of_accs = await query.message.chat.ask(f'Toplam hesaplarınız {len(accounts)}, Kaç hesap kullanılsın :')








        hesap_time =await query.message.chat.ask('Kaç dakika sonra tekrardan başlasın ?:')
        await hesap_time.request.edit_text(f"Döngü süresi : {hesap_time.text}")






        existing_accs = []
        to_use = [x for x in accounts[:int(number_of_accs.text)]]
        for l in to_use: accounts.remove(l)
        with open('hesaplar.txt', 'wb') as f:
            for a in accounts:
                pickle.dump(a, f)
            for ab in to_use:
                pickle.dump(ab, f)
            f.close()
        sleep_time = await query.message.chat.ask('Saniye başı mesaj gönderme süresi seç :')
        await sleep_time.request.edit_text(f"Yeniden başlama süresi : {sleep_time.text}")

        bilgi = f' -- Başlıyor Kullanılan Hesap {len(to_use)} --'
        adding_status = 0
        approx_members_count = 0

        ckimlik=query.message.chat.id
        mkimlik=query.message.id
        loadbar = await app.send_message(query.message.chat.id, 'İşlem başlatılıyor')
        await app.send_message(chat_id=query.message.chat.id, text="Autograph", reply_markup=iptal)

        # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        while True:

                for acc in to_use:


                      stop = index + 60
                      c =  TelegramClient(f'sessions/{acc[0]}', 3910389, '86f861352f0ab76a251866059a6adbd6')
                      bilgi = f'{acc[0]} Oturum başlatılıyor '
                      await c.connect()
                      acc_name =(await c.get_me()).first_name



                      peer_flood_status = 0
                      i = 0
                      dialogs =await c.get_dialogs()
                      for dialog in dialogs:
                          if dialog.is_group :
                              i += 1

                      if i >= 1 :
                          for dialog in dialogs:
                              if dialog.is_group :

                                  try:
                                      await c.send_message(dialog.id,mesaj)


                                      adding_status += 1







                                  except PeerFloodError:
                                      hatabilgi =f'Kullanıcı: {acc_name} -- Flood Hatası.'
                                      peer_flood_status += 1

                                      continue
                                  except ChatWriteForbiddenError:
                                      hatabilgi=f'{dialog.title}-->Mesaj göndermeye kapalı'


                                  except UserBannedInChannelError:
                                      hatabilgi=f'Kullanıcı: {acc_name} -- Gruba Yazmanız Kısıtlandı'

                                      break
                                  except ChatAdminRequiredError:

                                      hatabilgi=f'Kullanıcı: {acc_name} -- Mesaj göndermek için Sohbet Yöneticisi Olman Gerekli'

                                      continue

                                  except FloodWaitError as e:
                                      hatabilgi=f'Gruba {e.seconds} saniye sonra mesaj yazılabilecek'

                                      break
                                  except ValueError:
                                      hatabilgi=f' Kişi Hatası'


                                      continue
                                  except KeyboardInterrupt:
                                      hatabilgi=f' ---- Ekleme sona erdi'

                                  except Exception as e:
                                      hatabilgi=f'{e}'

                                      continue

                              else:
                                  break


                              text=f"⚙️ Durum : {bilgi}\n👤 Kullanılan hesap : {acc_name}\n===================================\n👁️‍🗨️ Gönderilen grup : {dialog.title}\n💬 Toplam gönderilen mesaj : {adding_status}\n⛔ Flood hatası : {peer_flood_status}\n🚫 Hata bilgi : {hatabilgi}"
                              await loadbar.edit_text(f"{text}")
                      c.disconnect()


                if "{}".format(user_register_dict["data"]['name']) == "False":
                    break

                print("beklemeye girdi")
                await asyncio.sleep(int(hesap_time.text)*60)
                print("bekleme bitti")



    elif query.data == "bomba":

     user_register_dict["data"]['name'] = "True"
     gruplar=[]

     await client.delete_messages(message.chat.id, [message.id])

     accounts = []
     f = open('hesaplar.txt', 'rb')
     while True:
          try:
             accounts.append(pickle.load(f))
          except EOFError:
              break;
     a = open('gruplar.txt', 'rb')
     while True:
         try:
             gruplar.append(pickle.load(a))

         except EOFError:
             break
     for grup in gruplar:
         print(grup[0])
     if len(accounts)==0:
          text = "Hata : Hiç hesap eklemedin"
          await app.send_message(query.message.chat.id, text, reply_markup=main_menu)
     elif len(gruplar)==0:
         text = "Hata : Hiç grup eklemedin"
         await app.send_message(query.message.chat.id, text, reply_markup=main_menu)

     else:

        await app.send_message(query.message.chat.id, "Engellenmiş hesaplar kontrol ediliyor..")
        for a in accounts:
            phn = a[0]

            clnt = TelegramClient(f'sessions/{phn}', 3910389, '86f861352f0ab76a251866059a6adbd6')
            await clnt.connect()
            banned = []
            if not await clnt.is_user_authorized():
                try:
                    await clnt.send_code_request(phn)

                except PhoneNumberBannedError:
                    await app.send_message(query.message.chat.id, f' {phn} Banlandı !')
                    banned.append(a)
            for z in banned:
                accounts.remove(z)
                await app.send_message(query.message.chat.id, "Engellenmiş hesaplar silindi...")
            time.sleep(1)
            clnt.disconnect()









        f = open('message.txt', 'r', encoding='utf-8')
        mesaj = f.read()
        accounts = []
        f = open('hesaplar.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(f))
            except EOFError:
                break

        index = 1
        bilgi = "none"
        hatabilgi = "Henüz hata yok"
        # tüm hesapları yükle (telefon numaraları)
        accounts = []

        f = open('hesaplar.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(f))
            except EOFError:
                break

        number_of_accse = await query.message.chat.ask(f'Toplam hesaplarınız {len(accounts)}, Kaç hesap kullanılsın :')



        existing_accs = []
        to_use = [x for x in accounts[:int(number_of_accse.text)]]
        for l in to_use: accounts.remove(l)
        with open('hesaplar.txt', 'wb') as f:
            for a in accounts:
                pickle.dump(a, f)
            for ab in to_use:
                pickle.dump(ab, f)
            f.close()
        sleep_timem = await query.message.chat.ask('Bittikten sonra kaç dakika sonra başlasın :')
        await sleep_timem.request.edit_text(f"Yeniden başlama süresi : {sleep_timem.text}")

        fotom = await query.message.chat.ask('Fotoğraf eklensinmi(evet/hayır) :')
        await fotom.request.edit_text(f"Fotoğraf eklensinmi : {fotom.text}")




        bilgi = f'  Başlıyor Kullanılan Hesap {len(to_use)} '
        adding_status = 0
        acc_name="None"
        approx_members_count = 0
        peer_flood_status=0

        ckimlik = query.message.chat.id
        mkimlik = query.message.id
        loadbar = await app.send_message(query.message.chat.id, 'İşlem başlatılıyor')
        await app.send_message(chat_id=query.message.chat.id, text="Durdurmak için bas", reply_markup=iptal)
        print("dsennenekfnk")

        # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        while True:
           for grup in gruplar:
             for acc in to_use:
               if "{}".format(user_register_dict["data"]['name']) == "True":



                   c = TelegramClient(f'sessions/{acc[0]}', 3910389, '86f861352f0ab76a251866059a6adbd6')
                   bilgi = f'{acc[0]}  Oturum başlatılıyor.. '
                   await c.connect()
                   acc_name = (await c.get_me()).first_name

                   try:
                       if '/joinchat/' in grup[0]:
                           g_hash = grup[0].split('/joinchat/')[1]
                           try:
                               await c(ImportChatInviteRequest(g_hash))
                               bilgi = f'{acc_name}  Mesaj göndermek için gruba katıldı '
                           except UserAlreadyParticipantError:
                               pass
                       else:
                           await c(JoinChannelRequest(grup[0]))

                           bilgi = f'{acc_name}  Mesaj göndermek için gruba katıldı '




                   except Exception as e:
                       bilgi = f'{acc_name}  Gruba katılamadı '
                       print(f' {e}')
                       break
                   bilgi = f'{acc_name}  Mesaj Gönderme başladı..'






                   index += 1

                   if peer_flood_status == 10:
                       break
                   try:

                       if fotom.text=="evet":
                        try:
                         photo_path = 'photo/photo.jpg'
                         await c.send_file(grup[0], photo_path, caption=mesaj)
                        except ValueError:
                            user_register_dict["data"]['name'] = "False"
                            await app.send_message(chat_id=query.message.chat.id, text="Hata : fotoğraf eklemedin",
                                                   reply_markup=main_menu)

                       else:
                         await c.send_message(grup[0], mesaj)
                       adding_status=adding_status+1



                       hatabilgi = "Yok"


                       durum = f' Kullanıcı: {acc_name} -- Uyku {sleep_timem.text}  Saniye(s)'




                   except UserPrivacyRestrictedError:
                       hatabilgi = f'Kullanıcı: {acc_name} -- Hata Kullanıcı Gizliliği Kısıtlı'

                       continue
                   except PeerFloodError:
                       hatabilgi = f'Kullanıcı: {acc_name} -- Flood Hatası.'

                       peer_flood_status += 1

                       continue
                   except ChatWriteForbiddenError:

                       hatabilgi = f'Gruba Üye Eklenemiyor. Üye eklemeyi etkinleştirmek için grup yöneticisiyle iletişime geçin'


                   except UserBannedInChannelError:
                       hatabilgi = f'Kullanıcı: {acc_name}  Gruba Yazmanız Kısıtlandı'

                       break
                   except ChatAdminRequiredError:

                       hatabilgi = f'Kullanıcı: {acc_name}  Üye Eklemek için Sohbet Yöneticisi Olman Gerekli'

                       continue
                   except UserAlreadyParticipantError:

                       hatabilgi = f'Kullanıcı: {acc_name}  Kullanıcı Zaten Eklendi'


                       continue
                   except FloodWaitError as e:
                       hatabilgi = f'{e}'


                       break
                   except ValueError:
                       print(f' Kişi Hatası')


                       break
                   except KeyboardInterrupt:
                       hatabilgi = f'  Ekleme sona erdi'


                       break

                   except Exception as e:
                       hatabilgi = f' {e}'





                   c.disconnect()
               text = f"Durum : {bilgi}\n===================================\n👤 Kullanılan hesap : {acc_name}:{acc[0]}\n👁️‍🗨️ Gönderilen grup : {grup[0].replace('https://t.me/','')}\n💬 Gönderilen mesaj : {adding_status}\n⛔ Flood hatası : {peer_flood_status}\n🚫 Hata bilgi : {hatabilgi}"
               await loadbar.edit_text(f"{text}")

           if "{}".format(user_register_dict["data"]['name']) == "False":

                     break

           await asyncio.sleep(int(sleep_timem.text)*60)








    elif query.data == "foto":
      user_register_dict["data"]['name'] = "True"

      await client.delete_messages(message.chat.id, [message.id])

      accounts = []
      f = open('hesaplar.txt', 'rb')
      while True:
          try:
              accounts.append(pickle.load(f))
          except EOFError:
              break
      if len(accounts) == 0:
          text = "Hata : Hiç hesap eklemedin"
          await app.send_message(query.message.chat.id, text, reply_markup=main_menu)

      else:
        await app.send_message(query.message.chat.id, "Engellenmiş hesaplar kontrol ediliyor..")
        for a in accounts:
            phn = a[0]

            clnt = TelegramClient(f'sessions/{phn}', 3910389, '86f861352f0ab76a251866059a6adbd6')
            await clnt.connect()
            banned = []
            if not await clnt.is_user_authorized():
                try:
                    await clnt.send_code_request(phn)

                except PhoneNumberBannedError:
                    await app.send_message(query.message.chat.id, f' {phn} Banlandı !')
                    banned.append(a)
            for z in banned:
                accounts.remove(z)
                await app.send_message(query.message.chat.id, "Engellenmiş hesaplar silindi...")
            time.sleep(1)
            clnt.disconnect()


        f = open('message.txt', 'r',encoding='utf-8')
        mesaj = f.read()
        accounts = []
        f = open('hesaplar.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(f))
            except EOFError:
                break

        index = 1
        bilgi = "none"
        hatabilgi = "Henüz hata yok"
        # tüm hesapları yükle (telefon numaraları)
        accounts = []

        f = open('hesaplar.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(f))
            except EOFError:
                break

        print(f' Toplam Hesaplarınız: ')
        number_of_accs = await query.message.chat.ask(f'Toplam hesaplarınız {len(accounts)}, Kaç hesap kullanılsın :')





        hesap_time =await query.message.chat.ask('Kaç dakika sonra tekrardan başlasın ?:')
        await hesap_time.request.edit_text(f"Döngü süresi : {hesap_time.text}")



        existing_accs = []
        to_use = [x for x in accounts[:int(number_of_accs.text)]]
        for l in to_use: accounts.remove(l)
        with open('hesaplar.txt', 'wb') as f:
            for a in accounts:
                pickle.dump(a, f)
            for ab in to_use:
                pickle.dump(ab, f)
            f.close()
        sleep_time = await query.message.chat.ask('Saniye başı mesaj gönderme süresi seç :')
        await sleep_time.request.edit_text(f"Yeniden başlama süresi : {sleep_time.text}")

        bilgi = f' -- Başlıyor Kullanılan Hesap {len(to_use)} --'
        adding_status = 0
        approx_members_count = 0

        ckimlik=query.message.chat.id
        mkimlik=query.message.id
        loadbar = await app.send_message(query.message.chat.id, 'İşlem başlatılıyor..')
        await app.send_message(chat_id=query.message.chat.id, text="Autograph", reply_markup=iptal)

        # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        while True:

                for acc in to_use:


                    stop = index + 60
                    c =  TelegramClient(f'sessions/{acc[0]}', 3910389, '86f861352f0ab76a251866059a6adbd6')
                    bilgi = f'{acc[0]}  Oturum başlatılıyor.. '
                    await c.connect()
                    acc_name =(await c.get_me()).first_name



                    peer_flood_status = 0
                    i = 0
                    dialogs =await c.get_dialogs()
                    for dialog in dialogs:
                        if dialog.is_group:
                            i += 1
                    if i >= 1 :
                        for dialog in dialogs:
                            if dialog.is_group:

                                time.sleep(int(sleep_time.text))
                                try:
                                    photo_path = 'photo/photo.jpg'
                                    await c.send_file(dialog.id, photo_path, caption=mesaj)


                                    adding_status += 1







                                except PeerFloodError:
                                    hatabilgi =f'Kullanıcı: {acc_name} -- Flood Hatası.'
                                    peer_flood_status += 1

                                    continue
                                except ChatWriteForbiddenError:
                                    hatabilgi=f'{dialog.title}-->Mesaj göndermeye kapalı'


                                except UserBannedInChannelError:
                                    hatabilgi=f'Kullanıcı: {acc_name} -- Gruba Yazmanız Kısıtlandı'

                                    break
                                except ChatAdminRequiredError:

                                    hatabilgi=f'Kullanıcı: {acc_name} -- Mesaj göndermek için Sohbet Yöneticisi Olman Gerekli'

                                    continue

                                except FloodWaitError as e:
                                    hatabilgi=f'Gruba {e.seconds} saniye sonra mesaj yazılabilecek'

                                    break
                                except ValueError:
                                    hatabilgi=f' Kişi Hatası'


                                    continue
                                except KeyboardInterrupt:
                                    hatabilgi=f'  Ekleme sona erdi'

                                except Exception as e:
                                    hatabilgi=f'{e}'

                                    continue
                            else:
                                break


                            text=f"⚙️ Durum : {bilgi}\n===================================\n👤Kullanılan hesap : {acc_name}\n👁️‍🗨️Gönderilen grup : {dialog.title}\n💬 Toplam gönderilen mesaj : {adding_status}\n⛔ Flood hatası : {peer_flood_status}\n🚫 Hata bilgi : {hatabilgi}"
                            await loadbar.edit_text(f"{text}")
                    c.disconnect()

                if "{}".format(user_register_dict["data"]['name']) == "False":
                    break

                print("beklemeye girdi")
                await asyncio.sleep(int(hesap_time.text)*60)
                print("bekleme bitti")





    elif query.data == "grupmenu":
        await query.edit_message_reply_markup(reply_markup=grupmenu)

    elif query.data == "add_grup":
        new_accs = []
        with open('gruplar.txt', 'ab') as g:
            await query.edit_message_reply_markup(reply_markup=None)
            number = await query.message.chat.ask('Lütfen bir grup girin (örn = https://t.me)')
            await number.request.edit_text(f"Grup linki : {number.text}")

            if number.text.find("https://t.me")==-1:
                await app.send_message(chat_id=query.message.chat.id, text="Lütfen geçerli bir grup linki girin", reply_markup=grupmenu)
            else:

                parsed_number = ''.join(number.text.split())
                pickle.dump([parsed_number], g)
                new_accs.append(parsed_number)
                text = "Grup eklendi."
                await app.send_message(chat_id=query.message.chat.id, text=text, reply_markup=grupmenu)





        g.close()


        # Mesajı gönder, inline keyboard'ı yanıt olarak ekle





    elif query.data == "add_number":

        new_accs = []
        with open('hesaplar.txt', 'ab') as g:
            await query.edit_message_reply_markup(reply_markup=None)
            number = await query.message.chat.ask('Lütfen bir numara girin (örn:+90)')
            await number.request.edit_text(f"Numara : {number.text}")



            c = TelegramClient(f'sessions/{number.text}', 3910389, '86f861352f0ab76a251866059a6adbd6')
            await c.connect()

            # Session açma
            if not await c.is_user_authorized():

                try:
                  try:
                    await c.send_code_request(number.text)
                    code = await query.message.chat.ask('Gelen kodu girin :')
                    await code.request.edit_text(f"Kod : {code.text}")
                    await c.sign_in(number.text, code.text)
                    await code.reply(f'Giriş başarılı', quote=True)
                    parsed_number = ''.join(number.text.split())
                    pickle.dump([parsed_number], g)
                    new_accs.append(parsed_number)
                    await query.edit_message_reply_markup(reply_markup=numaramenu)
                  except PhoneCodeInvalidError:
                      code = await query.message.chat.ask('Yanlış kod girdiniz lütfen tekrar gir :')
                      await code.request.edit_text(f"Kod : {code.text}")
                      await c.sign_in(number.text, code.text)
                      await code.reply(f'Giriş başarılı', quote=True)
                      parsed_number = ''.join(number.text.split())
                      pickle.dump([parsed_number], g)
                      new_accs.append(parsed_number)

                      await query.edit_message_reply_markup(reply_markup=numaramenu)
                except SessionPasswordNeededError:
                    sifre = await query.message.chat.ask('Hesap şifresini girin :')
                    await sifre.request.edit_text(f"Şifre : {sifre.text}")
                    await c.sign_in(password=sifre.text)
                    await sifre.reply(f'Giriş başarılı', quote=True)
                    parsed_number = ''.join(number.text.split())
                    pickle.dump([parsed_number], g)
                    new_accs.append(parsed_number)



                except PhoneNumberInvalidError:
                    number = await query.message.chat.ask('Yanlış numara, Lütfen bir numara girin (örn:+90)')
                    await number.request.edit_text(f"Numara : {number.text}")
                except Exception as e:
                    await app.send_message(query.message.chat.id, f"Hata lütfen tekrar deneyin")
                    await query.edit_message_reply_markup(reply_markup=numaramenu)
                finally:
                    await c.disconnect()




        g.close()
        text = "Numara menü"

        # Mesajı gönder, inline keyboard'ı yanıt olarak ekle
        await app.send_message(chat_id=query.message.chat.id, text=text, reply_markup=numaramenu)
  else:
      await client.answer_callback_query(
          callback_query_id=query.id,
          text="Bu botu kullanmaya yetkin yok!"
      )


app.run()
