import arrow

a = arrow.get()
arrow.get('1958-11-19')
arrow.now('America/Sao_Paulo')
a.to('local')
a.to('US/Eastern')
a.shift('hours=2')

import humanize
eu = arrow.get('1958-11-19')
agora = arrow.get()
idade = agora - eu
idade
humanize.naturaldelta(idade)
humanize.i18n.activate('pt_BR')
humanize.naturaldelta(idade)
