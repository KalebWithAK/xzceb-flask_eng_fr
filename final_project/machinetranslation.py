from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import ApiException
import json

authenticator = IAMAuthenticator('PmEt7Vi63_nRsVvR4Bkz0pPVEUi-QA0g7Lh_XL0fKQce')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/820802b0-dbe3-4a36-9941-db4c06162661')

language_translator.set_disable_ssl_verification(False)


def translator(text, languages):
  try:
    translation = language_translator.translate(text=text, model_id=languages).get_result()

    return json.loads(json.dumps(translation, indent=2, ensure_ascii=False))['translations'][0]['translation']
  except ApiException as ex:
      print("Method failed with status code " + str(ex.code) + ": " + ex.message)


#print(translator('hello, how are you today?', 'en-fr'))