from system.Lib import *
import subprocess
import csv

Clear()

cfg_path = './system/cfg.json'

def select_lang():
    global string
    lang = input(
            'Select Language\n'
            'Выберите язык\n\n'
            '1 - English\n'
            '2 - Русский\n\n>>> ')
    if lang == '1':
        lang = 'en'
    elif lang == '2':
        lang = 'ru'
    else:
        Clear()
        select_lang()

    config.update({'lang': lang})
    json.dump(config, open(cfg_path, 'w'))
    from system.strings import string
    string = string[config['lang']]


def init(ret=True):
    if ret:
        Clear()
    info(string.detected_os % platform.system())
    info(string.installing)
    [os.system(f'pip3 install {i}{nul}') for i in ['colorama', 'pillow', 'lzma', 'pylzham', 'sc_compression']]
    info(string.crt_workspace)
    [[os.makedirs(f'SC/{i}-{k}', exist_ok=True) for k in ['Compressed', 'Decompressed', 'Sprites']] for i in ['In', 'Out']]
    [[os.makedirs(f'CSV/{i}-{k}', exist_ok=True) for k in ['Compressed', 'Decompressed']] for i in ['In', 'Out']]
    [[os.makedirs(f'convert sc/{i}-{k}', exist_ok=True) for k in ['Sc', 'Json']] for i in ['In', 'Out']]
    [[os.makedirs(f'Compress/{i}-{k}', exist_ok=True) for k in ['Uncompressing', 'Uncompressed']] for i in ['For', 'Out']]
    info(string.verifying)
    for i in ['colorama', 'PIL', 'lzma', 'lzham']:
        try:
            [exec(f"{k} {i}") for k in ['import', 'del']]
            info(string.installed % i)
        except:
            info(string.not_installed % i)

    config.update({'inited': True})
    json.dump(config, open(cfg_path, 'w'))
    if ret:
        input(string.to_continue)

def ccp_encode():
    global errors
    folder = './Compress/For-Uncompressing/'
    folder_export = './Compress/Out-Uncompressed/'

    for i in os.listdir(folder):
        try:
            compileSC_not_lzma(f"{folder}{i}/", folder_export=folder_export)
        except Exception as e:
            errors += 1
            err_text(string.err % (e.__class__.__module__, e.__class__.__name__, e))
            write_log(traceback.format_exc())

        print()

def clear_dirs():
    for i in ['In', 'Out']:
        for k in ['Compressed', 'Decompressed', 'Sprites']:
            folder = f'SC/{i}-{k}'
            if os.path.isdir(folder):
                shutil.rmtree(folder)
            os.makedirs(folder, exist_ok=True)

    for i in ['In', 'Out']:
        for k in ['Compressed', 'Decompressed']:
            folder = f'CSV/{i}-{k}'
            if os.path.isdir(folder):
                shutil.rmtree(folder)
            os.makedirs(folder, exist_ok=True)
    
    for i in ['In', 'Out']:
        for k in ['Sc', 'Json']:
            folder = f'convert sc/{i}-{k}'
            if os.path.isdir(folder):
                shutil.rmtree(folder)
            os.makedirs(folder, exist_ok=True)

    for i in ['For', 'Out']:
        for k in ['Uncompressing', 'Uncompressed']:
            folder = f'Compress/{i}-{k}'
            if os.path.isdir(folder):
                shutil.rmtree(folder)
            os.makedirs(folder, exist_ok=True)



def sc_decode():
    global errors
    folder = "./SC/In-Compressed-SC/"
    folder_export = "./SC/Out-Decompressed-SC/"

    for file in os.listdir(folder):
        if file.endswith("_tex.sc"):

            CurrentSubPath = file[::-1].split('.', 1)[1][::-1] + '/'
            if os.path.isdir(f"{folder_export}{CurrentSubPath}"):
                shutil.rmtree(f"{folder_export}{CurrentSubPath}")
            os.mkdir(f"{folder_export}{CurrentSubPath}")
            try:
                decompileSC(f"{folder}{file}", CurrentSubPath, folder = folder, folder_export = folder_export)
            except Exception as e:
                errors += 1
                err_text(string.err % (e.__class__.__module__, e.__class__.__name__, e))
                write_log(traceback.format_exc())

            print()
            
def sc2js_by_zrm():
                    file_name = input((string.fn))
                    file_name = file_name + ".json"
                    subprocess.call(['python', 'system/sc2json v2.py', 'sc2json', file_name])
                    
def js2sc_by_zrm():
                    file_name = input((string.fn))
                    file_name = file_name + ".sc"
                    subprocess.call(['python', 'system/sc2json v2.py', 'sc2json', file_name])

def sc_encode():
    global errors
    folder = './SC/In-Decompressed-SC/'
    folder_export = './SC/Out-Compressed-SC/'

    for i in os.listdir(folder):
        try:
            compileSC(f"{folder}{i}/", folder_export=folder_export)
        except Exception as e:
            errors += 1
            err_text(string.err % (e.__class__.__module__, e.__class__.__name__, e))
            write_log(traceback.format_exc())

        print()
        
def server():
	subprocess.call(['python','./Core.py'])
    
def scw_tool():
    subprocess.call(['python', 'system/scw.py'])


def sc1_decode():
    global errors
    folder = "./SC/In-Compressed-SC/"
    folder_export = "./SC/Out-Sprites-SC/"
    files = os.listdir(folder)

    for file in files:
        if file.endswith("_tex.sc"):

            scfile = file[:-7] + '.sc'
            if scfile not in files:
                err_text(string.not_found % scfile)
            else:
                CurrentSubPath = file[::-1].split('.', 1)[1][::-1] + '/'
                if os.path.isdir(f"{folder_export}{CurrentSubPath}"):
                    shutil.rmtree(f"{folder_export}{CurrentSubPath}")
                os.mkdir(f"{folder_export}{CurrentSubPath}")
                try:
                    info(string.dec_sctex)
                    sheetimage, xcod = decompileSC(f"{folder}{file}", CurrentSubPath, to_memory=True, folder_export=folder_export)
                    info(string.dec_sc)
                    spriteglobals, spritedata, sheetdata = decodeSC(f"{folder}{scfile}", sheetimage)
                    xc = open(f"{folder_export}{CurrentSubPath}" + file[:-3] + '.xcod', 'wb')
                    xc.write(xcod)
                    cut_sprites(spriteglobals, spritedata, sheetdata, sheetimage, xc, f"{folder_export}{CurrentSubPath}")
                except Exception as e:
                    errors += 1
                    err_text(string.err % (e.__class__.__module__, e.__class__.__name__, e))
                    write_log(traceback.format_exc())

            print()
            
def forpin():
    subprocess.call(['python', 'system/pin.py']) 
            
def voucher():
            	x = input("Укажите название воучера: ")

            	print("Ваш воучер:")

            	print("https://link.brawlstars.com/ru?action=voucher&code=" + x)

def decompress_csv():
	try:
		from sc_compression import Decompressor, Compressor
	except ImportError:
		from sc_compression.compression import Decompressor, Compressor
		
	for filename in os.listdir('CSV/In-Compressed/'):
		with open(f'CSV/In-Compressed/{filename}', 'rb') as fh:
			filedata = fh.read()
			fh.close()
		decompressor = Decompressor()
		decompressed = decompressor.decompress(filedata)
		with open(f'CSV/Out-Decompressed/{filename}', 'wb') as fh:
			fh.write(decompressed)
			fh.close()
	
indir = './CSV/In-Compressed/'
outdir = './CSV/Out-Decompressed/'

def colors():
    global color
    COLORNAME = input(
            'By @rostchannel2\n'
            'Выберите цвет\n'
            '1 - КРАСНЫЙ\n'
            '2 - ЗЕЛЕНЫЙ\n'
            '3 - ЖЕЛТЫЙ\n'
            '4 - СИНИЙ\n'
            '5 - ФИОЛЕТОВЫЙ\n'
            '6 - КУАН\n\nВаш выбор>>')
    if COLORNAME == '1':
        color = 'RED'
        subprocess.call(['python', 'system/change color/to red.py'])
        print((string.restart_script))
        quit()
    elif COLORNAME == '2':
        color = "GREEN"
        subprocess.call(['python', 'system/change color/to green.py'])
        print((string.restart_script))
        sys.exit
    elif COLORNAME == '3':
        color = 'YELLOW'
        subprocess.call(['python', 'system/change color/to yellow.py'])
        print((string.restart_script))
        Clear()
    elif COLORNAME == '4':
        color = 'BLUE'
        subprocess.call(['python', 'system/change color/to blue.py'])
        print((string.restart_script))
        sys.exit
    elif COLORNAME == '5':
        color = 'MAGENTA'
        subprocess.call(['python', 'system/change color/to magenta.py'])
        print((string.restart_script))
        sys.exit
    elif COLORNAME == '6':
        color = 'CYAN'
        subprocess.call(['python', 'system/change color/to cyan.py'])
        print((string.restart_script))
        sys.exit
    else:
        Clear()
        colors()
        
    config.update({'color': color})
    json.dump(config, open(cfg_path, 'w'))
    color = color[config['color']] 


def compress_csv():
    from sc_compression.signatures import Signatures

    folder = './CSV/In-Decompressed'
    folder_export = './CSV/Out-Compressed'

    for file in os.listdir(folder):
        if file.endswith('.csv'):
            try:
                with open(f'{folder}/{file}', 'rb') as f:
                    file_data = f.read()
                    f.close()

                with open(f'{folder_export}/{file}', 'wb') as f:
                    f.write(compress(file_data, Signatures.LZMA))
                    f.close()
            except Exception as exception:
                logger.exception(locale.error % (exception.__class__.__module__, exception.__class__.__name__, exception))

            print()
            
def to_json():
                    file_name = input((string.fnf))
                    file_name = file_name + ".sc"
                    subprocess.call(['python', 'system/sc2json.py', 'sc2json', file_name])
                    
            
def to_sc():
                    file_name = input((string.fnf))
                    file_name = file_name + ".json"
                    subprocess.call(['python', 'system/sc2json.py', 'json2sc', file_name])
 
def unlocks():
    subprocess.call(['python', './system/hack.py'])
    
def sc_decode2():
    global errors
    folder = "./SC/In-Compressed-SC/"
    folder_export = "./SC/Out-Decompressed-SC/"

    for file in os.listdir(folder):
        if file.endswith("_tex.sc"):

            CurrentSubPath = file[::-1].split('.', 1)[1][::-1] + '/'
            if os.path.isdir(f"{folder_export}{CurrentSubPath}"):
                shutil.rmtree(f"{folder_export}{CurrentSubPath}")
            os.mkdir(f"{folder_export}{CurrentSubPath}")
            try:
                decompileSC2(f"{folder}{file}", CurrentSubPath, folder = folder, folder_export = folder_export)
            except Exception as e:
                errors += 1
                err_text(string.err % (e.__class__.__module__, e.__class__.__name__, e))
                write_log(traceback.format_exc())
               
    print()
    
def mp42sc():
    subprocess.call(['python', 'mp42sc.py'])
    
def sc2mp4():
    subprocess.call(['python', './sc2mp4.py'])
    

def sc1_encode():
    global errors
    folder = "SC/In-Sprites-SC/"
    folder_export = "SC/Out-Compressed-SC/"
    files = os.listdir(folder)

    for file in files:
        print(file)

        xcod = file + '.xcod'
        if xcod not in os.listdir(f'{folder}{file}/'):
            err_text(string.not_found % xcod)
        else:
            
            try:
                info(string.dec_sctex)
                sheetimage, sheetimage_data = place_sprites(f"{folder}{file}/{xcod}", f"{folder}{file}")
                info(string.dec_sc)
                compileSC(f'{folder}{file}/', sheetimage, sheetimage_data, folder_export)
            except Exception as e:
                errors += 1
                err_text(f"Пошел нахуй! ({e.__class__.__module__}.{e.__class__.__name__}: {e})")
                write_log(traceback.format_exc())
            print()


v = Version

if __name__ == '__main__':
    if os.path.isfile(cfg_path):
        try:
            config = json.load(open(cfg_path))
        except:
            config = {'inited': False, 'version': v}
    else:
        config = {'inited': False, 'version': v}

    if not config.get('lang'):
        select_lang()

    if not config['inited']:
        init()
        try: os.system('python%s "%s"' % ('' if isWin else '3', __file__))
        except: pass
        exit()

    from system.strings import string, console
    Title(string['en'].zcoder % config['version'])

    while 1:
        try:
            string = string[config['lang']]
            break
        except:
            select_lang()

    locale(config['lang'])
    

    while 1:
        try:
            errors = 0
            [os.remove(i) if os.path.isfile(
                i) else None for i in ('temp.sc', '_temp.sc')]
            
            Clear()
            answer = console(config)
            print()
            if answer == '1':
                sc_decode()
            elif answer == '2':
                sc_encode()
            elif answer == '3':
                sc1_decode()
            elif answer == '4':
                sc1_encode()
            elif answer == '5':
                sc_decode2()
            elif answer == '6':
                sc_decode()
                ccp()
            elif answer == '6':
             	decompress_csv()
            elif answer == '7':
            	 compress_csv()
            elif answer == '8':
             	to_json()
            elif answer == '9':
            	 to_sc()
            elif answer == '10':
            	 sc2js_by_zrm()
            elif answer == '11':
            	 js2sc_by_zrm
            elif answer == '12':
             	sc2mp4()
            elif answer == '13':
            	 mp42sc()
            elif answer == '14':
                 scw_tool()
            elif answer == '15':
                 unlocks()

            elif answer == '101':
                print(string.not_implemented)
            elif answer == '102':
                init(ret=False)
            elif answer == '105':
                 voucher()
            elif answer == '106':
            	 colors()
            elif answer == '103':
                select_lang()
                locale(config['lang'])
            elif answer == '104':
                if not question(string.clear_qu):
                    continue
                clear_dirs()
                    
            elif answer == '100':
                Clear()
                break

            else:
                continue

            if errors > 0:
                err_text(string.done_err % errors)
            else:
                done_text(string.done)

            input(string.to_continue)
        
        except KeyboardInterrupt:
            if question(string.want_exit):
                Clear()
                break
