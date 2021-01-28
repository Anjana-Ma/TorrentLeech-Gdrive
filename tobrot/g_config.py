from tobrot.sample_config import Config

#Fill your all data, read readme for reference

#FOR CUSTOM COMMANDS READ REAME AND FILL THEM...

class Config(Config):
    TG_BOT_TOKEN= "1521484417:AAEHFILFqvEYAO8A-GiVA02PntFccYghgVI"
    APP_ID = 2710778
    API_HASH = "a3e5503b94be442badc605ca7905c83c"
    OWNER_ID = 1468099476
    AUTH_CHANNEL = [-1001283185883]
    DESTINATION_FOLDER = "TorrentLeech-Gdrive" #Name of your folder read readme(not id of the folder)
    #Just don't fill RCLONE_CONFIG vars, insted copy your rclone.conf file in root directory
    #if your wanted to fill -- fill your rclone config like this(Your config may have some extra value or less. so Don't worry)
    RCLONE_CONFIG = """
[Torrent Leech]
type = drive
client_id = 595329019144-17ommms2dt354ddsq7kf9abg8ommk3o4.apps.googleusercontent.com
client_secret = 1uy9jkw9KKDFUzSzrphv1tvq
scope = drive
root_folder_id = 1jRz24hTH6kdOz_42zKsPPtu8fmT0l0Jv
token = {"access_token":"ya29.a0AfH6SMD4TKTwinkqbhdxxrYuMZ8DUIgjmkeCBKGadtkGdNQH3aJ-E81evF3sFX27UtC6Vm_vC1SeMMfMfKzB68I5gma04MP5tNYhrEftu3x6fxF9XJbypwZI5q-mCTdG4ZCc4T_-eITYC3DMXLINrGIWHlpndJ0wwjwtC77CspI","token_type":"Bearer","refresh_token":"1//0g-nyTA6YFvAdCgYIARAAGBASNwF-L9IrR4gDYIapeqq-ptPei49YS4IHlmgnWb6mr5nvvaSww3JVafH6Kdt6L4qdNU1jOBl38hw","expiry":"2021-01-28T14:06:17.0615914+05:30"}
"""