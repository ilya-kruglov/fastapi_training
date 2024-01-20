from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class PrompterHint(BaseModel):
    actor: str
    replica: str

    class Config:
        title = 'Class for send_prompt'
        schema_extra = {
            'examples': {
                'kolobok': {
                    'summary': 'Колобок',
                    'value': {
                        'actor': 'Медведь',
                        'replica': 'Колобок, колобок, я тебя съем!'
                    }
                },
                'hamlet': {
                    'summary': 'Гамлет, принц датский',
                    'value': {
                        'actor': 'Гамлет',
                        'replica': 'Бедный Йорик! Я знал его, Горацио.'
                    }
                },
                'palata_number_6': {
                    'summary': 'Палата номер 6',
                    'value': {
                        'actor': 'Рагин',
                        'replica': 'Покой и довольство человека не вне его, '
                                   'а в нём самом.'
                    }
                }
            }
        }


@app.post('/give-a-hint')
def send_prompt(
        hint: PrompterHint = Body(
            ...,
            examples=PrompterHint.Config.schema_extra['examples']
        )
) -> PrompterHint:
    return hint
