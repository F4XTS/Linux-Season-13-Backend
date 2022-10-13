# ECLIPTIC S13 Backend was created by noteason
#gay balz
#
#arra0x & kparser = SKID 
#arra0x like big asian men fucking him
#cum
import os

os.system("pip install BoogieFN")

import sanic
import BoogieFN #reks dnt exist
import json
from sanic_ipware import get_client_ip
import os
import requests
import aiohttp
import datetime
import shutil
from datetime import datetime as d

"""noteason was here :)""" #very true

"""defining a few things needed"""

app = sanic.Sanic("S13")
path = "cloudstorage" #this is the path where the cloudstorage files are - noteason
cloudstorage = BoogieFN.generate_cloudstorage(path, json=json) #generates cloudstorage config -noteason

DefaultEngine = open(f"{path}/DefaultEngine.ini").read()
  
DefaultGame = open(f"{path}/DefaultGame.ini").read()
  
DefaultRuntimeOptions = open(f"{path}/DefaultRuntimeOptions.ini").read()


notFound = {
	"errorCode": "errors.com.epicgames.common.not_found",
	"errorMessage": "Sorry the resource you were trying to find could not be found",
	"messageVars": [],
	"numericErrorCode": 150,
	"originatingService": "fortnite",
	"intent": "prod-live"
}

async def ac_log(request):
  ip, routable = get_client_ip(request)
  print(f"[13.40] | [{request.method}] {request.path}")

async def get_profile(accountid):
  dirr = f'config/profiles/{accountid}'
  #make file if doesnt exist
  if os.path.exists(dirr) == False:
    os.makedirs(dirr)
    shutil.copyfile('templates/def.json', dirr+'/settings.json')
  #load config file
  with open(dirr+'/settings.json') as f:
    account_settings = json.load(f)
  return account_settings

@app.route('/')
async def main(request):
  return sanic.response.json({"LINUX": "13.40"})


"""cloudstorage endpoints"""

@app.route('/fortnite/api/cloudstorage/system')
async def cldstrg(request): #make sure nothing is defined as cloudstorage or this endpoint will not work
  await ac_log(request)
  return sanic.response.json(cloudstorage)

@app.route('/fortnite/api/cloudstorage/system/DefaultEngine.ini')
async def de(request):
  await ac_log(request)
  return sanic.response.raw(DefaultEngine)

@app.route('/fortnite/api/cloudstorage/system/DefaultGame.ini')
async def dg(request):
  await ac_log(request)
  return sanic.response.raw(DefaultGame)

@app.route('/fortnite/api/cloudstorage/system/DefaultRuntimeOptions.ini')
async def dro(request):
  await ac_log(request)
  return sanic.response.raw(DefaultRuntimeOptions)

@app.route('/fortnite/api/cloudstorage/system/config')
async def syscon(request):
  await ac_log(request)
  return await sanic.response.file("cloudconfig.json")

"""api endpoints"""

@app.route('/fortnite/api/v2/versioncheck/<version>')
async def versioncheck(request, version):
  await ac_log(request)
  return sanic.response.json({"type":"NO_UPDATE"})

@app.route('/fortnite/api/game/v2/enabled_features')
async def enabled(request):
  await ac_log(request)
  return sanic.response.json([])

@app.route('/fortnite/api/storefront/v2/catalog')
async def shop(request):
  await ac_log(request)
  return sanic.response.json(json.load(open("items.json")))

@app.route('/datarouter/api/v1/public/data')
async def datarouter(request):
  await ac_log(request)
  return sanic.response.json(notFound)

@app.route('/fortnite/api/calendar/v1/timeline')
async def timeline(request):
  await ac_log(request)
  return await sanic.response.file("timeline.json")

@app.route('/socialban/api/public/v1/<accountid>')
async def socialban(request, accountid):
  await ac_log(request)
  return sanic.response.empty()

@app.route('/fortnite/api/storefront/v2/keychain')
async def keychain(request):
  await ac_log(request)
  return sanic.response.redirect("https://api.nitestats.com/v1/epic/keychain")


"""fortnite-game generator made by noteason"""
def generate_game():
  r = requests.get("https://fortnitecontent-website-prod07.ol.epicgames.com/content/api/pages/fortnite-game").json()
  r['emergencynotice']['news']['messages'] = [{
          "gamemodes": [
            "stw",
            "br"
          ],
          "hidden": False,
          "_type": "CommonUI Emergency Notice Base",
          "title": f"Welcome To Linux Season 13!",
          "body": f"Made by noteason#0001"
        }]
  
  r['dynamicbackgrounds']['backgrounds']['backgrounds'] = {
  "stage": "season13",
  "_type": "DynamicBackground",
  "key": "lobby"
  },
  {
  "stage": "default",
  "_type": "DynamicBackground",
  "key": "vault"
  }
  r['battleroyalenews']['news']['motds'] = [{
                        "entryType": "Website",
                        "image": "https://cdn.discordapp.com/attachments/1002954773735153664/1028369941558202449/Picsart_22-10-08_19-14-54-175.jpg",
                        "tileImage": "https://cdn.discordapp.com/attachments/1002954773735153664/1028369941558202449/Picsart_22-10-08_19-14-54-175.jpg",
                        "videoMute": False,
                        "hidden": False,
                        "tabTitleOverride": "Linux S13",
                        "_type": "CommonUI Simple Message MOTD",
                        "title": "Linux S13",
                        "body": "Made using noteason's S13 Backend",
                        "videoLoop": False,
                        "videoStreamingEnabled": False,
                        "sortingPriority": 0,
                        "id": "NEWSLOL",
                        "videoAutoplay": False,
                        "videoFullscreen": False,
                        "spotlight": False,
                        "websiteURL": "https://dsc.gg/LinuxFN",
                        "websiteButtonText": "Discord Server"
                    }]
  return r

@app.route('/content/api/pages/fortnite-game')
async def news(request):
  await ac_log(request)
  fortnite_game = generate_game()
  return sanic.response.json(fortnite_game)
  
@app.route("/content/api/pages/fortnite-game/media-events")
async def media_events(request):
  await ac_log(request)
  return sanic.response.json([])


"""matchmaking stuff **i did not make i got it from a friend**"""

@app.route('fortnite/api/matchmaking/session/<sid>', methods=['POST', 'GET'])
async def test(request,sid: str):
		await ac_log(request)
		reqbody = request.body
		reqheader = request.headers
		paramz = request.args
		res = requests.get('https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/matchmaking/session/'+sid+'', headers=reqheader)
		resjson = json.loads(res.text)
		resheaders = res.headers
		return sanic.response.json(resjson, headers=resheaders)
@app.route('fortnite/api/matchmaking/session/<sid>/<met>', methods=['POST', 'GET'])
async def test(request,sid: str,met: str):
		await ac_log(request)
		reqbody = request.body
		reqheader = request.headers
		paramz = request.args
		res = requests.get('https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/matchmaking/session/'+sid+'', params=paramz, headers=reqheader)
		resheaders = res.headers
		return sanic.response.json(json.loads(res.text), headers=resheaders)

@app.route('fortnite/api/game/v2/matchmakingservice/ticket/player/<sid>/', methods=['POST', 'GET'])
async def test(request,sid: str):
		await ac_log(request)
		reqbody = request.body
		reqheader = request.headers
		request.args['player.platform'] = 'Android'
		paramz = request.args
		res = requests.get('https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/matchmakingservice/ticket/player/'+sid+'', params=paramz, headers=reqheader)
		resjson = json.loads(res.text)
		resheaders = res.headers
		return sanic.response.text(res.text, headers=resheaders)



def locker_shit(accountid):
	id = accountid
	with open(f"config/profiles/{id}/settings.json") as f:
		try:
			settings = json.load(f)
		except Exception as e:
			print(e)
	locker = {"default_loadout": {
						"attributes": {
							"banner_color_template": settings.get("banner_colour"),
							"banner_icon_template": settings.get("banner"),
							"favorite": True,
							"item_seen": False,
							"locker_name": "LINUX_BETA",
							"locker_slots_data": {
								"slots": {
									"Backpack": {
										"activeVariants": [
											{
												"variants": []
											}
										],
										"items": [
											settings.get("backpack")
										]
									},
									"Character": {
										"activeVariants": [
											{
												"variants": settings.get("skin_variants")
											}
										],
										"items": [
											settings.get("character")
										]
									},
									"Dance": {
										"items": [
											settings.get("emote0"),
											settings.get("emote1"),
											settings.get("emote2"),
											settings.get("emote3"),
											settings.get("emote4"),
											settings.get("emote5")
										]
									},
									"Glider": {
										"activeVariants": [
											{
												"variants": []
											}
										],
										"items": [
											settings.get("glider")
										]
									},
									"ItemWrap": {
										"activeVariants": [
											[
												{
													"variants": []
												}
											],
											[
												{
													"variants": []
												}
											],
											[
												{
													"variants": []
												}
											],
											[
												{
													"variants": []
												}
											],
											[
												{
													"variants": []
												}
											],
											[
												{
													"variants": []
												}
											],
											[
												{
													"variants": []
												}
											]
										],
										"items": [
											settings.get("wrap0"),
											settings.get("wrap1"),
											settings.get("wrap2"),
											settings.get("wrap3"),
											settings.get("wrap4"),
											settings.get("wrap5"),
											settings.get("wrap6")
										]
									},
									"LoadingScreen": {
										"activeVariants": [
											{
												"variants": []
											}
										],
										"items": [
											settings.get("loadingscreen")
										]
									},
									"MusicPack": {
										"activeVariants": [
											{
												"variants": []
											}
										],
										"items": [
											settings.get("music")
										]
									},
									"Pickaxe": {
										"activeVariants": [
											{
												"variants": []
											}
										],
										"items": [
											settings.get("pickaxe")
										]
									},
									"SkyDiveContrail": {
										"activeVariants": [
											{
												"variants": []
											}
										],
										"items": [
											settings.get("contrail")
										]
									}
								}
							},
							"use_count": 1
						},
						"quantity": 1,
						"templateId": "CosmeticLocker:cosmeticlocker_athena"
					}
				}
	return locker

async def render_athena(
	accountid,
	change=False
):
	accountid
	with open("templates/template.json") as f:
		old_json=json.load(f)
	async with aiohttp.ClientSession() as session:
		async with session.get('https://fortnite-api.com/v2/cosmetics/br/') as response:
			jsonresponse = await response.json()
	items = jsonresponse['data']
	for item in items:
		id = item['id']
		backendtype = item['type']['backendValue']
		if item['variants'] == None:
			v = []
		else:
			v = []
			for material in item['variants']:
				i = {
					"channel": None,
					"active": None,
					"owned": []
				}
				i['channel'] = material['channel']
				i['active'] = material['options'][0]['tag']
				for mat in material['options']:
					i['owned'].append(mat['tag'])
				v.append(i)
		now = d.now()
		current_time = now.strftime("%H:%M:%S")
		old_json['profileChanges'][0]['profile']['items'].update(
			{
				f"{backendtype}:{id}": {
						"attributes": {
							"favorite": False,
							"item_seen": True,
							"level": 1,
							"max_level_bonus": 0,
							"rnd_sel_cnt": 0,
							"variants": v,
							"xp": 0
						},
						"quantity": 1,
						"templateId": f"{backendtype}:{id}",
						"purchaseDate": "2069-06-08T17:22:19.592Z"
				}
			}
		)
	async with aiohttp.ClientSession() as session:
		async with session.get('https://fortnite-api.com/v2/cosmetics/br/new') as response:
			jsonresponse = await response.json()
	items = jsonresponse['data']['items']
	for item in items:
		id = item['id']
		backendtype = item['type']['backendValue']
		if item['variants'] == None:
			v = []
		else:
			v = []
			for material in item['variants']:
				i = {
					"channel": None,
					"active": None,
					"owned": []
				}
				i['channel'] = material['channel']
				i['active'] = material['options'][0]['tag']
				for mat in material['options']:
					i['owned'].append(mat['tag'])
				v.append(i)
		now = d.now()
		current_time = now.strftime("%H:%M:%S")
		old_json['profileChanges'][0]['profile']['items'].update(
			{
				f"{backendtype}:{id}": {
						"attributes": {
							"favorite": False,
							"item_seen": False,
							"level": 1,
							"max_level_bonus": 0,
							"rnd_sel_cnt": 0,
							"variants": v,
							"xp": 0
						},
						"quantity": 1,
						"templateId": f"{backendtype}:{id}",
						"purchaseDate": "2069-06-08T17:22:19.592Z"
				}
			}
		)
    
#ignore my super shitty coding -noteason
	with open(f"config/profiles/{accountid}/settings.json") as f:
		settingz = json.load(f)
	old_json['profileChanges'][0]['profile']['items'].update(locker_shit(accountid=accountid))
	old_json['profileChanges'][0]['profile']['_id'] = accountid
	old_json['profileChanges'][0]['profile']['accountId'] = accountid
	old_json['profileChanges'][0]['profile']['created'] = f"{datetime.date.today()} {current_time}"
	old_json['serverTime'] = f"{datetime.date.today()} {current_time}"
	if change == True:
		settingz['profileRevision'] += 1
		old_json['profileRevision'] = settingz['profileRevision']
		goofy_ahh = settingz['profileRevision']
		old_json['profileChangesBaseRevision'] = goofy_ahh
		old_json['profileCommandRevision'] = goofy_ahh
	else:
		settingz['profileRevision'] == 0
		old_json['profileRevision'] = settingz['profileRevision']
  #crown
	old_json['profileChanges'][0]['profile']['items']['VictoryCrown:defaultvictorycrown']['attributes']['victory_crown_account_data']['total_royal_royales_achieved_count'] = settingz['crowns']
  #level
	old_json['profileChanges'][0]['profile']['stats']['attributes']['level'] = settingz['level']
  #stars
	old_json['profileChanges'][0]['profile']['stats']['attributes']['battlestars'] = settingz['battlestars']
  #style points
	old_json['profileChanges'][0]['profile']['stats']['attributes']['style_points'] = settingz['style_points']
	with open(
		f"config/profiles/{accountid}/settings.json",
		"w"
	) as f_:
		json.dump(
			settingz,
			f_,
			indent=2
		)
	return old_json  


async def update_user_settings(
	id:str,
	type,
	itemToSlot,
	bannerColorTemplateName=None,
	slot=None,
	variants=[],
):
	with open(f"config/profiles/{id}/settings.json") as f:
		settings = json.load(f)
	print(type)
	if bannerColorTemplateName != None and itemToSlot != None and type == "banner":
		settings['banner'] = itemToSlot
		settings['banner_colour'] = bannerColorTemplateName
	elif type in [
		'emote',
		'wrap'
	]:
		settings[type + str(slot)] = itemToSlot
	elif type != None and itemToSlot != None:
		settings["skin_variants"] = variants
		settings[type] = itemToSlot
    


	with open(
		f"config/profiles/{id}/settings.json",
		"w"
	) as f_:
		json.dump(
			settings,
			f_,
			indent=2
		)
	return await render_athena(
		accountid=id,
		change=True
	)

async def create_creative(accountid, rvn):
  with open("templates/creative.json") as f:
    creative_json=json.load(f)
  creative_json['rvn'] = int(rvn)
  creative_json['_id'] = accountid
  creative_json['accountId'] = accountid
  
  return creative_json

async def create_common_core(accountid, rvn, account_settings):
  now = d.now()
  current_time = now.strftime("%H:%M:%S")
  with open("templates/change.json") as f:
    change=json.load(f)
  change['profileChanges'][0]['profile']['rvn'] = rvn
  change['profileChanges'][0]['profile']['_id'] = accountid
  change['profileChanges'][0]['profile']['accountId'] = accountid
  change['profileChanges'][0]['profile']['created'] = f"{datetime.date.today()} {current_time}"
  change['profileChanges'][0]['profile']['items']['Currency:MtxPurchased']['quantity'] = str(account_settings['v-bucks'])
  return change

async def create_collections(accountid):
  now = d.now()
  current_time = now.strftime("%H:%M:%S")
  with open("templates/collections.json") as f:
    collections = json.load(f)
  collections['serverTime'] = f"{datetime.date.today()} {current_time}"
  collections['profileChanges'][0]['profile']['created'] = f"{datetime.date.today()} {current_time}"
  collections['profileChanges'][0]['profile']['_id'] = accountid
  collections['profileChanges'][0]['profile']['accountId'] = accountid
  return collections  
  
async def create_common_core(accountid, rvn, account_settings):
  now = d.now()
  current_time = now.strftime("%H:%M:%S")
  with open("templates/change.json") as f:
    change=json.load(f)
  change['profileChanges'][0]['profile']['rvn'] = rvn
  change['profileChanges'][0]['profile']['_id'] = accountid
  change['profileChanges'][0]['profile']['accountId'] = accountid
  change['profileChanges'][0]['profile']['created'] = f"{datetime.date.today()} {current_time}"
  change['profileChanges'][0]['profile']['items']['Currency:MtxPurchased']['quantity'] = str(account_settings['v-bucks'])
  return change



@app.route('/fortnite/api/game/v2/profile/<accountid>/client/<command>', methods=['POST', 'GET'])
async def var(request,accountid: str,command: str):
  await ac_log(request)
  now = d.now()
  current_time = now.strftime("%H:%M:%S")
  rvn = request.args['rvn'][0]

  #get account settings
  account_settings = await get_profile(accountid)
  
  if request.args.get("profileId") == 'creative' and command == 'QueryProfile':
    creative_json = await create_creative(accountid, rvn)
    return sanic.response.json(creative_json)
    
  elif request.args.get("profileId") == 'common_core' and command == 'QueryProfile':
    common_core_json = await create_common_core(accountid, rvn, account_settings)
    return sanic.response.json(common_core_json)

  elif request.args.get("profileId") == "common_core" and command == 'SetMtxPlatform':
    common_core_json = await create_common_core(accountid, rvn, account_settings)
    return sanic.response.json(common_core_json)
    
  elif request.args.get("profileId") == "common_core" and command == 'VerifyRealMoneyPurchase':
    common_core_json = await create_common_core(accountid, rvn, account_settings)
    return sanic.response.json(common_core_json)

  elif request.args.get("profileId") == "common_core" and command == 'ClaimMfaEnabled':
    common_core_json = await create_common_core(accountid, rvn, account_settings)
    return sanic.response.json(common_core_json)

  elif request.args.get("profileId") == 'common_public' and command == 'QueryProfile':
    return sanic.response.json([])

  elif request.args.get("profileId") == 'collections' and command == 'QueryProfile':
    collections = await create_collections(accountid)
    return sanic.response.json(collections)

  if request.args.get("profileId") == 'athena' and command == 'QueryProfile':
    old_json = await render_athena(accountid=accountid)
    return sanic.response.json(old_json)
  elif request.args.get("profileId") == "athena" and command == 'SetHardcoreModifier':
    old_json = await render_athena(accountid=accountid)
    return sanic.response.json(old_json)

  elif request.args.get("profileId") == "athena" and command == 'ClientQuestLogin':
    return sanic.response.json(json.loads('{"profileRevision":6888,"profileId":"athena","profileChangesBaseRevision":6888,"profileChanges":[],"serverTime":"2021-03-29T19:04:47.462Z","profileCommandRevision":2618,"responseVersion":1}'))
    
  elif request.args.get("profileId") == "athena" and command == 'MarkItemSeen':
    return sanic.response.json({"errorCode":"errors.com.epicgames.mcpprofilegroup.backend","errorMessage":"Oops Looks Like BoogieFN's Bakcned Caused an issue!","messageVars":[],"numericErrorCode":1004,"originatingService":"fortnite","intent":"prod-live"})

  elif command == 'SetCosmeticLockerBanner':
    new_json = await update_user_settings(
      id=accountid,
      type="banner",
      variants=request.json.get("variantUpdates"),
      bannerColorTemplateName=request.json.get("bannerColorTemplateName"),
      itemToSlot=request.json.get("bannerIconTemplateName")
    )
    return sanic.response.json(new_json)
	
  elif command == 'SetCosmeticLockerSlot':
      if request.json.get("category") == "AthenaEmoji":
        new_json = await update_user_settings(
          id=accountid,
          type="AthenaDance",
          slot=request.json.get("slotIndex"),
          variants=request.json.get("variantUpdates"),
          itemToSlot=request.json.get("itemToSlot")
        )
        return sanic.response.json(new_json) 
      typeget = {
  			"Dance": "emote",
  			"ItemWrap": "wrap",
  			"Backpack": "backpack",
  			"MusicPack": "music",
  			"Character": "character",
  			"LoadingScreen": "loadingscreen"
  		}
			#print(request.json)
      if typeget.get(request.json.get("category")):
        new_json = await update_user_settings(
          id=accountid,
          type=typeget.get(request.json.get("category")),
          slot=request.json.get("slotIndex"),
          variants=request.json.get("variantUpdates"),
          itemToSlot=request.json.get("itemToSlot")
  			) 
        return sanic.response.json(new_json)


app.run(host="0.0.0.0", port=1340, access_log=False)