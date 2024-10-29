import urllib3
from elasticsearch import Elasticsearch
import pandas as pd

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from utilis import gerar_embedding, gerar_indice, indexar_documentos, atualizar_rel_jur, buscar_documentos

es = Elasticsearch(
    ['https://localhost:9200'],
    basic_auth=('elastic', '19112023'),
    verify_certs=False  # Desabilitar a verificação do certificado para simplificar
)

# Testar a conexão
if es.ping():
    print("Conectado ao Elasticsearch!")
else:
    print("Falha na conexão.")

# Definir o nome do índice
index_name = 'documentos_juridicos'

df = pd.read_csv("../data/acordaos_reduzidos.csv")

gerar_indice(es, index_name)
indexar_documentos(es, df, index_name)


documento = """ESTADO DO CEARÁ
 
PODER JUDICIÁRIO
 TRIBUNAL DE JUSTIÇA
 
 
 
 
1Ş Turma Recursal
  
Nº PROCESSO: 3001466-38.2021.8.06.0118
 
CLASSE: RECURSO INOMINADO CÍVEL
 
RECORRENTE: JOSE FREDSON SILVA DE SOUZA
 
RECORRIDO: COMPANHIA DE AGUA E ESGOTO DO CEARA CAGECE
 
 
 
 
EMENTA:

 
ACÓRDÃO:
Vistos, relatados e discutidos os autos, acordam os membros da Primeira Turma Recursal dos Juizados Especiais Cíveis e Criminais do Estado do Ceará, por unanimidade, em conhecer do Recurso Inominado e negar-lhe provimento, nos termos do voto do relator (artigo 61 do Regimento Interno).
 
RELATÓRIO:

 
VOTO:



PODER JUDICIÁRIO DO ESTADO DO CEARÁ 

FÓRUM DAS TURMAS RECURSAIS PROFESSOR DOLOR BARREIRA

PRIMEIRA TURMA RECURSAL DOS JUIZADOS ESPECIAIS CÍVEIS E CRIMINAIS






RECURSO INOMINADO CÍVEL Nº 3001466-38.2021.8.06.0118

RECORRENTE: COMPANHIA DE ÁGUA E ESGOTO DO CEARÁ - CAGECE

RECORRIDO: JOSÉ FREDSON SILVA DE SOUZA

ORIGEM: JECC DA COMARCA DE MARACANAÚ/CE

RELATOR: JUIZ ANTONIO ALVES DE ARAUJO

 

 

 

 

 

EMENTA: RECURSO INOMINADO. RELAÇÃO DE CONSUMO. SERVIÇO DE ÁGUA E ESGOTO. CORTE NO FORNECIMENTO REFERENTE VIOLAÇÃO APURADA NO HIDRÔMETRO. IRREGULARIDADE PREEXISTENTE A TITULARIDA DO AUTOR. INCIDÊNCIA DO ARTIGO 116, §ÚNICO DA RESOLUÇÃO 130/2010 DA ARCE. CORTE INDEVIDO ANTES DO PRAZO PARA RECURSO ADMINISTRATIVO. ARTIGO 118, §2º DA RESOLUÇÃO 130/2010 DA ARCE. FALTA DE NOTIFICAÇÃO PRÉVIA. SUSPENSÃO INDEVIDA (ARTIGO 10, INCISO I, LEI 7.783/89). ATO ILÍCITO. DANOS MORAIS IN RE IPSA. CASO CONCRETO: 67 DIAS SEM ÁGUA. INDENIZAÇÃO ARBITRADA NO JUÍZO A QUO EM R$ 6.000,00. LONGO PERÍDO DE PRIVAÇÃO DO SERVIÇO ESSENCIAL. QUANTUM AQUÉM DO DEVIDO. MANTIDO POR VEDAÇÃO A REFORMATIO IN PEJUS. DECLARALÇAO DE INEXISTÊNCIA DA MULTA MANTIDA. RECURSO CONHECIDO E IMPROVIDO. CUSTAS E HONORÁRIOS EM 20% SOBRE O VALOR DA CONDENAÇÃO. SENTENÇA MANTIDA.





ACÓRDÃO



Vistos, relatados e discutidos os autos, acordam os membros da Primeira Turma Recursal dos Juizados Especiais Cíveis e Criminais do Estado do Ceará, por unanimidade, em conhecer do Recurso Inominado e negar-lhe provimento, nos termos do voto do relator (artigo 61 do Regimento Interno).

Fortaleza, 24 de julho de 2023.



ANTÔNIO ALVES DE ARAÚJO

Juiz Relator

 



 

RELATÓRIO



Tratam os autos de Recurso Inominado interposto pela Companhia de Água e Esgoto do Ceará (CAGECE), objetivando a reforma da sentença proferida pelo Juizado Especial da Cível e Criminal da Comarca de Maracanaú/CE, nos autos da Ação de Obrigação de Fazer c/c Pedido de Tutela Provisória Antecipada c/c Danos Morais, ajuizada em seu desfavor por José Fredson Silva de Souza.

Na inicial (ID. 4931376), narra a autora que, em 21/11/2020, solicitou uma transferência de titularidade, passando a ser responsável pela unidade consumidora de n. 009072888, a qual adimplia regularmente com os custos pela prestação de serviços de fornecimento de água e esgoto. Sustenta que recebeu uma notificação de corte, em 23/09/2021, por suposta violação de hidrômetro, sendo interrompido a distribuição de água em sua residência 3 (três) dias após a notificação. Com isso, argumenta que se dirigiu a uma agência de atendimento da ré, em 05/10/2021, momento que tomou conhecimento de uma multa no valor de R$ 4.520,00 (quatro mil, quinhentos e vinte reais), o que resultou na suspensão dos serviços de abastecimento de água por 23 (vinte e três) dias, até o ajuizamento da presente ação. Por essa razão, buscou a prestação da tutela jurisdicional para requerer indenização por dano moral em R$ 6.000,00 (seis mil reais) e declaração de inexistência da multa arbitrada pela empresa demandada.

Contestação no ID. 4931392.

Termo de audiência de conciliação, sem êxito (ID. 4931409).

Sobreveio sentença de procedência dos pedidos iniciais em que se reconheceu a responsabilidade civil da concessionária ré, fundamentando o juízo singular que é incabível a interrupção do fornecimento de água, em decorrência de multa, por não se tratar de inadimplência de fatura atual, além de apontar que a empresa requerida não logrou êxito em apresentar “ provas consistentes sobre os fatos imputados ao autor”, pelo que declarou a inexistência da multa no valor de R$ 4.520,00 (quatro mil, quinhentos e vinte reais) e arbitrou indenização por danos morais no valor de R$ 6.000,00 (seis mil reais) em favor do autor, devidamente atualizado pelo regime de juros legais de mora de 1% (um por cento) ao mês, desde a citação (artigo 405, do Código Civil) e correção monetária pelo INPC, desde a data da sentença (Súmula n.º 362, STJ), extinguindo o feito, com resolução de mérito, nos termos do artigo 487, inciso I do Código de Processo Civil (ID. 4931422).

No recurso inominado, argui que “ realizou verificação em setembro de 2021 sendo identificado que o hidrômetro estava com a cúpula furada e o lacre violado, por conta disso, no dia 27 daquele mesmo mês, a Cagece realizou o corte no fornecimento de água face a infração, aplicando corretamente uma multa” e que cabe a parte autora, na condição de titular da unidade consumidora, a responsabilidade por eventuais danos ou violações ao hidrômetro, na forma do Decreto Estadual 12.844/1978, bem como não foram comprovados danos morais e, ao fim, pede a reforma integral da sentença, para afasta a declaração de inexistência da multa (R$ 4.520,00) e a condenação em danos morais (R$ 6.000,00), apresentando pedido subsidiário de redução do valor indenizatório para valor não superior a um salário mínimo (ID. 4931426).

Não foram apresentadas contrarrazões, conforme certidão de ID. 4931437.

Remetido o caderno processual a esta Turma revisora, vieram-me os autos conclusos. É o relatório, decido. 



VOTO



Presentes os requisitos de admissibilidade dispostos nos artigos 42 e 54, §Ú da Lei nº 9.099/95, conheço do recurso.

Em respeito ao comando jurídico previsto no artigo 93, inciso IX, CF, passo a motivar e a fundamentar a decisão.



MÉRITO



À relação existente entre as partes é aplicável o Código de Defesa do Consumidor, por força dos artigos 2º e 3º e seu §2º, Lei 8.078/90.

Em princípio, ressalta-se que o autor é usuário do serviço de água e esgoto na unidade consumidora n. 009072888, que se consolidou mediante transferência de titularidade, solicitada em 21/11/2020 e teve o fornecimento de água cortado no dia 27/09/2021, três dias depois de ter recebido a notificação de corte, por motivo de irregularidade no hidrômetro, que resultou em multa no valor R$ 4.520,00 (quatro mil, quinhentos e vinte reais), conforme Solicitação de Orçamento Débitos e Serviços acostada ao ID. 4931377.

Do que consta nos autos, são fatos incontroversos o corte no fornecimento de água, em 27/09/2021 e o reestabelecimento somente em 03/12/2021, por força da decisão liminar do ID. 4931378.

Contudo, nota-se pelas nítidas irregularidades na apuração da irregularidade, a qual não notificou previamente o autor da realização da fiscalização. Além do que consta na fatura do antigo titular da unidade consumidora, referente ao mês de outubro de 2020, com a leitura do mês anterior em 91 metros cúbicos de água, realizada em 21/09/2020, e a leitura do mês de referência com valor idêntico de 91 metros cúbicos de água, realizada em 21/10/2020 (vide página 13 do ID. 4931377).

Curiosamente, a mesma leitura de 91 metros cúbicos se repete Termo de Ocorrência que apurou a suposta infração do promovente e na última fatura acostada pelo autor, com vencimento 11/10/2021, ou seja, mais de um ano antes a leitura de já estava em 91 metros cúbicos, antes mesmo do autor se tornar titular da unidade consumidora fiscalizada, fazendo concluir que a irregularidade era preexistente à posse do requente sobre o imóvel onde se localiza o hidrómetro violado, conforme se observa no contrato de locação do ID. 4931377.

Portanto, o corte do serviço extrapolou o regular exercício do direito de cobrança e incorreu em ato ilícito por falha na prestação do serviço público, ensejando lastro para responsabilização civil. O artigo 116, §único da Resolução 130, de 25 de março de 2010, da Agência Reguladora de Serviços Públicos Delegados do Estado do Ceará (ARCE), determina:

Art. 116

(...)

Parágrafo único - Comprovado pelo prestador de serviços ou a partir de provas documentais fornecidas pelo novo usuário, que o início da irregularidade ocorreu em período não atribuível ao responsável pela unidade usuária, o atual usuário somente será responsável pelas diferenças de volumes de água e de esgoto excedentes apuradas no período sob sua responsabilidade, e sem aplicação do disposto de multa, exceto nos casos de sucessão comercial.

Logo, pela simples comparação das faturas do titular anterior, em cotejo com as mensalidades em nome do autor, já seria possível concluir que o recorrido não poderia ser responsabilizado pela irregularidade preexistente.

Ademais, ficou demonstrado, ainda, a irregularidade no corte que ocorreu três dias após a lavratura do Termo de Ocorrência (ID. 4931377) e antes da notificação realizada no atendimento n. 156638287 (ID. 4931394), em patente violação ao artigo 118, §2º da Resolução 130, de 25 de março de 2010, da Agência Reguladora de Serviços Públicos Delegados do Estado do Ceará (ARCE):

Art. 118 - É assegurado ao infrator o direito de recorrer ao prestador de serviços, no prazo de 15 (quinze) dias, contados a partir do dia subsequente ao recebimento do auto de infração.

§ 1º - Da decisão cabe recurso à ARCE no prazo de 15 (quinze) dias contados da ciência da decisão do prestador de serviços.

§ 2º - Durante a apreciação do recurso pelo prestador ou pela ARCE, não haverá suspensão da prestação do serviço em função da matéria sob apreciação. (grifei).

Mesmo sem notificação prévia a fiscalização e antes do recebimento do auto de infração para início do prazo de recurso administrativo, a recorrente suspendeu indevidamente os serviços prestado ao autor.

Em consonância com as considerações sobre irregularidades apontadas, a jurisprudência do Tribunal de Justiça do Ceará também corrobora que o vício de falta de notificação prévia torna a fiscalização indevida, vejamos os precedentes:

EMENTA: DIREITO PROCESSUAL CIVIL. CONSUMIDOR APELAÇÃO CÍVEL. AÇÃO COMINATÓRIA C/C INDENIZATÓRIA POR DANOS MORAIS. FORNECIMENTO DE ÁGUA E ESGOTO. SUPOSTA IRREGULARIDADE DO HIDRÔMETRO. CORTE DO FORNECIMENTO DE ÁGUA. APLICAÇÃO DE MULTA POR SUPOSTA IRREGULARIDADE NO HIDRÔMETRO. RESPONSABILIDADE OBJETIVA (ART. 37, § 6º, DA CF/88 E NO ART. 14 DO CDC). INVERSÃO DO ÔNUS DE PROVA. CONCESSIONÁRIA NÃO SE DESINCUMBIU DO ÔNUS DO ART. 373, II, CPC/15. MULTA APLICADA PELA RÉ E SUSPENSÃO DO ABASTECIMENTO SÃO INDEVIDOS. FALHA NA PRESTAÇÃO DO SERVIÇO DA COMPANHIA. DANOS MORAIS DEVIDOS. QUANTUM MANTIDO. APELO CONHECIDO E IMPROVIDO. 4. In casu, verifica-se que a autora, ao receber, através da vizinha, um Termo de Ocorrência constando irregularidades no medidor (fl. 16), procurou a parte da suplicada para obter esclarecimentos, no entanto, naquela ocasião recebeu a informação de que havia uma negociação de dívida referente a multa que não deu causa, conforme fl. 17, sem que tenha havido qualquer informação prévia ou processo administrativo. Observa-se ainda, às fls. 24-33, que a autora continuava recebendo suas faturas normais de acordo com a média de consumo normal, até o momento que houve o corte do fornecimento de água em sua residência, por um suposto gato no medidor. 5. Destaca-se que a realização do termo de ocorrência, na residência da suplicante, se deu sem qualquer notificação prévia, da mesma forma que no próprio termo não consta a assinatura da autora. Ademais, ressalta-se que não há nenhum documento anexado pela concessionária que comprove a referida acusação de irregularidades no hidrômetro. 6. Tem-se que a parte ré não logrou êxito em apresentar fatos extintivos do direito autoral, ônus que lhe incumbia, nos termos do art. 14, § 3º do CDC e do art. artigo 373, inciso II, do Código de Processo Civil. Assim, a manutenção da sentença é medida que se impõe. 7. Ademais, no que diz respeito ao quantum indenizatório, tem-se que o valor de R$ 8.000,00 (oito mil reais), arbitrado pelo Juízo de origem atende aos princípios da proporcionalidade e razoabilidade, uma vez que a parte autora passou aproximadamente 10 (dez) dias sem o fornecimento de água em sua unidade consumidora, não merecendo portanto qualquer redução. Da mesma forma que a atualização monetária deverá ocorrer consoante a disposição da Súmula 362 do STJ, conforme determinado em sentença de Piso. (Apelação Cível - 0050203-81.2021.8.06.0132, Rel. Desembargador(a) MARIA DE FÁTIMA DE MELO LOUREIRO, 2ª Câmara Direito Privado, data do julgamento:  26/10/2022, data da publicação:  26/10/2022).

É devida, portanto, a indenização moral, pois o prejuízo sofrido é presumido pela própria interrupção ilícita do serviço de água, nos termos do artigo 10, inciso I da lei nº 7.783/1989, o qual deveria ser fornecido de forma contínua (artigo 22 do CDC), pois integra o conceito de dignidade da pessoa humana.

No caso, o recorrido ficou mais de dois meses privado indevidamente do fornecimento de água (de 27/09/2021 a 03/12/2021), sendo legítima a pretensão de reparação moral em R$ 6.000,00 (seis mil reais), embora aquém do quantum devido e em descompasso com os princípios da proporcionalidade e da razoabilidade, deve ser mantido por vedação a reformatio in pejus, uma vez que houve privação abusiva de um serviço público essencial, por extenso período (mais de dois meses), mas único recurso manejado foi interposto pela parte ré.

Por fim, com base nas irregularidade apontada acima, também deve ser mantida a declaração de inexistência da multa de R$ 4.520,00 (quatro mil quinhentos e vinte reais).



DISPOSITIVO



Diante do exposto, CONHEÇO DO RECURSO INOMINADO PARA NEGAR-LHE PROVIMENTO e confirmo a sentença nos termos em que proferida.

Condeno a parte recorrente vencida ao pagamento das custas legais e honorários advocatícios, estes arbitrados em 20% sobre o valor da condenação, a teor do disposto no artigo 55 da Lei nº 9.099/95.

Fortaleza/CE, 24 de julho de 2023.




ANTÔNIO ALVES DE ARAÚJO

Juiz Relator"""

resultados = buscar_documentos(es, index_name, documento)
for res in resultados:
    print(res)
