import re

from .models import Spare, stops




def parsing(*, book):

    data = []

    for sheet in book.sheets():

        if sheet.name.strip() not in stops:

            counter = sheet.nrows - 3

            for row in range(counter):

                item = [sheet.cell_value(rowx=3+row, colx=j) for j in range(5)]

                article = str(item[0]).replace(' ', '')

                if article and article not in ['АРТИКУЛ', 'SANICUBIC 2 XL VX TRI - 2018']:

                    spare = Spare(
                                refference = re.sub("^\s+|\n|\r|\s+$", '', str(item[0]).strip().replace(' ', '')),
                                position = [re.sub("^\s+|\n|\r|\s+$", '', item[1].strip()) if type(item[1]) == str else round(item[1]),] or None,
                                ru_name = str(item[2]).strip(),
                                en_name = str(item[3]).strip(),
                                price = round(float(re.sub("^\s+|\n|\r|\s+$", '', str(item[4]).strip().replace(' ', '')))) if str(item[4]).strip().replace(' ', '') not in ['Уточняется', '', ' '] else 0,
                                group = [sheet.name.strip(),]
                    )

                    obj = [item for item in data if item.refference == spare.refference] or None

                    if obj:

                        group_name = sheet.name.strip()

                        if group_name not in obj[0].group:
                            obj[0].group.append(sheet.name.strip())

                        if spare.position[0] not in obj[0].position:
                            obj[0].position.append(spare.position[0])


                    else:
                        data.append(spare)

    return data