from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import ApiException
import json
import os
from dotenv import load_dotenv

load_dotenv()


api_key = os.environ.get('API_KEY')
url = os.environ.get('API_URL')

authenticator = IAMAuthenticator(api_key)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

language_translator.set_disable_ssl_verification(False)


def translator(text, languages):
  try:
    translation = language_translator.translate(text=text, model_id=languages).get_result()

    return json.loads(json.dumps(translation, indent=2, ensure_ascii=False))['translations'][0]['translation']
  except ApiException as ex:
      print("Method failed with status code " + str(ex.code) + ": " + ex.message)
