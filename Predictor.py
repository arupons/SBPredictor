from Plate import Plate
from datetime import datetime
from RestrictionConfig import PYPD as DayRestrictions
from RestrictionConfig import PYPH as HourRestrictions


class Predictor:

    def predict(self, plate, date, time):
        result = {}
        if Plate().validate(plate):
            dateFormat = '%Y-%m-%d %H:%M'
            try:
                formattedDate = datetime.strptime(
                    date + " " + time, dateFormat)
                if int(plate[-1]) in DayRestrictions[formattedDate.strftime('%A')]:
                    dayRestrictionStart = datetime.strptime(
                        date + " " + HourRestrictions['Day'][0], dateFormat)
                    dayRestrictionEnd = datetime.strptime(
                        date + " " + HourRestrictions['Day'][1], dateFormat)

                    if formattedDate > dayRestrictionStart and formattedDate < dayRestrictionEnd:
                        result['msg'] = "Your vehicle with plate " + plate + " can not circulate on the date " + \
                            date + " at " + time + ", you have to wait until " + \
                            str(dayRestrictionEnd) + " to circulate."
                        result['success'] = False
                    else:
                        nightRestrictionStart = datetime.strptime(
                            date + " " + HourRestrictions['Night'][0], dateFormat)
                        nightRestrictionEnd = datetime.strptime(
                            date + " " + HourRestrictions['Night'][1], dateFormat)
                        if formattedDate > nightRestrictionStart and formattedDate < nightRestrictionEnd:
                            result['msg'] = "Your vehicle with plate " + plate + " can not circulate on the date " + \
                                date + " at " + time + ", you have to wait until " + \
                                str(nightRestrictionEnd) + " to circulate."
                            result['success'] = False
                        else:
                            result['msg'] = "Your vehicle with plate " + plate + " can circulate on the date " + \
                                date + " at " + time
                            result['success'] = False
                else:
                    result['msg'] = "Your vehicle with plate " + \
                        plate + " can circulate on the date " + date + " at any time."
                    result['success'] = True
            except ValueError:
                result['msg'] = "Incorrect data format, date must be YYYY-MM-DD (Year-Month-Day)"
                result['success'] = False
        else:
            result['msg'] = 'Incorrect data format, Plate must be valid, example: ABC-1234, ABC-123'
            result['success'] = False
        return result
