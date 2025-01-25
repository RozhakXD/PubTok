try:
    import requests, json, re, random, string, os
    from requests_toolbelt import MultipartEncoder
    from rich import print as Println
    from rich.panel import Panel
    from rich.console import Console
except ModuleNotFoundError as error:
    exit(f"[Error] {str(error).capitalize()}!")

def BANNER() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    Println(
        Panel(r"""[bold red] ●[bold yellow] ●[bold green] ●[/]
[bold green] ,--------.,--.,--.    ,------.               ,--. 
 '--.  .--'`--'|  |,-. |  .---',--.,--. ,---. |  | 
    |  |   ,--.|     / |  `--, |  ||  || .-. :|  | 
    |  |   |  ||  \  \ |  |`   '  ''  '\   --.|  | 
[bold green]    `--'   `--'`--'`--'`--'     `----'  `----'`--' 
        [underline white]Free Tiktok Followers - by Rozhak""", width=55, style="bold bright_white"
        )
    )
    return

def INSERT_TIKTOK_LINK() -> None:
    try:
        BANNER()
        Println(Panel(f"[bold white]Silakan Masukkan Username Tiktok Yang Ingin Diberi\nkan Followers,\nPastikan Akun Tersebut Tidak Dalam Mode Pribadi!", width=55, style="bold bright_white", title="[bold bright_white]>> [Your Username] <<", subtitle="[bold bright_white]╭──────", subtitle_align="left"))
        username = Console().input("[bold bright_white]   ╰─> ").replace('@', '')
        SENDING_FOLLOWERS(username)
        exit()
    except Exception as error:
        Println(Panel(f"[bold red]{str(error).title()}!", width=55, style="bold bright_white", title="[bold bright_white]>> [Error] <<"))
        exit()

def SENDING_FOLLOWERS(username: str) -> bool:
    with requests.Session() as session:
        session.headers.update(
            {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-language': 'en-US,en;q=0.9',
                'connection': 'keep-alive',
                'host': 'tikfuel.com',
                'upgrade-insecure-requests': '1',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'user-agent': GENERATE_USER_AGENT(),
            }
        )
        response = session.get('https://tikfuel.com/free-tt/', allow_redirects=True, verify=True)
        try:
            wpforms_post_id = re.search(r'name="wpforms\[post_id\]" value="(\d+)"', response.text).group(1)
            wpforms_id = re.search(r'name="wpforms\[id\]" value="(\d+)"', response.text).group(1)
            data_token = re.search(r'data-token="(.*?)"', response.text).group(1)
            wpforms_fields = re.search(r'name="wpforms\[fields\]\[4\]\[\]" value="(.*?)"', response.text).group(1)
            wpforms_submit = re.search(r'name="wpforms\[submit\]" id="(.*?)"', response.text).group(1)
        except AttributeError:
            Println(Panel(f"[bold red]Maaf, Layanan Ini Sudah Tidak Berfungsi Lagi, Kare\nna Server Mengalami Masalah\nSaat Memproses Pengikut. Silakan Coba Lagi Nanti!", width=55, style="bold bright_white", title="[bold bright_white]>> [Servers Down] <<"))
            return False
        boundary = '----WebKitFormBoundary' + ''.join(random.sample(string.ascii_letters + string.digits, 16))

        session.headers.update(
            {
                'content-type': 'multipart/form-data; boundary={}'.format(boundary),
                'referer': 'https://tikfuel.com/free-tt/',
                'sec-fetch-site': 'same-origin',
                'cache-control': 'max-age=0',
                'origin': 'https://tikfuel.com',
                'cookie': ("; ".join([str(key) + "=" + str(value) for key, value in session.cookies.get_dict().items()]))
            }
        )

        fake_email = f'{"".join(random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(8))}@gmail.com'
        fake_strings = "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(8))

        data = MultipartEncoder({
            'wpforms[fields][3]': (None, f'@{username}'),
            'wpforms[fields][1]': (None, fake_strings),
            'wpforms[fields][2]': (None, fake_email),
            'wpforms[fields][4][]': (None, wpforms_fields),
            'wpforms[id]': (None, wpforms_id),
            'wpforms[author]': (None, '1'),
            'wpforms[post_id]': (None, wpforms_post_id),
            'wpforms[submit]': (None, wpforms_submit),
            'wpforms[token]': (None, data_token)
        }, boundary = boundary)

        response2 = session.post('https://tikfuel.com/free-tt/', data=data, verify=True, allow_redirects=False)

        if 'Our systems detected that you already used once our program for Free Followers.' in response2.text:
            Println(Panel(f"[bold red]Maaf, Sistem Kami Mendeteksi Bahwa Anda Telah Mengg\nunakan Program Kami Untuk Pengikut Gratis. Gunak\nanlah Username Yang Berbeda Untuk Mencoba Kembali!", width=55, style="bold bright_white", title="[bold bright_white]>> [Username Limits] <<"))
            return False
        elif 'Estimated delivery time' in response2.text or 'First time submission' in response2.text:
            Println(Panel(f"""[bold white]Status :[bold green] Successfully...
[bold white]Followers :[bold yellow] -+25
[bold white]Link :[bold red] https://www.tiktok.com/@{username}""", width=55, style="bold bright_white", title="[bold bright_white]>> [Success] <<"))
            return True
        else:
            Println(Panel(f"[bold red]Maaf, Server Kami Mengalami Masalah Saat Mengirimk\nan Pengikut, Silakan Coba Beberapa Saat Lagi!", width=55, style="bold bright_white", title="[bold bright_white]>> [Server Errors] <<"))
            return False

def GENERATE_USER_AGENT() -> str:
    browser_version = f'{random.randrange(101, 108)}.0.{random.randrange(4200, 4900)}.{random.randrange(40, 150)}'
    byte = random.choice(['Win64; x64', 'Win32; x86'])

    return f"Mozilla/5.0 (Windows NT 10.0; {byte}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{browser_version} Safari/537.36"

if __name__ == '__main__':
    try:
        os.system("git pull")
        if not os.path.exists("Penyimpanan/Subscribe.json"):
            youtube_url = json.loads(requests.get('https://raw.githubusercontent.com/RozhakXD/TikFuel/refs/heads/main/Penyimpanan/Youtube.json').text)['Link']
            os.system(f'xdg-open {youtube_url}')
            with open('Penyimpanan/Subscribe.json', 'w') as w:
                json.dump({"Status": True}, w, indent=4)
        INSERT_TIKTOK_LINK()
        exit()
    except KeyboardInterrupt:
        exit()