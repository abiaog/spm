#!/bin/python3

import datetime
import logging

logger = logging.getLogger('Auto')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('run.log')
fh.setLevel(logging.DEBUG) 
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


logger.debug('debug message')


class WeekGenerator(object):
    def __init__(self, year):
        self.year = year
        self.yearShort = self.year[len(self.year) - 2:]
        self.tji_filename = 'week' + self.year + '.tji'
        logger.debug('File name ' + self.tji_filename + ' was generated.')

    def produce_weeks(self):
        tji = open(self.tji_filename, 'w')
        logger.debug(self.tji_filename + ' was opened.')
        for w in range(0, 54):
            for d in range(0,7):
                week = self.year + '-w' + str(w)
                if w <=9:
                    week_display = 'w' + self.yearShort + '0' + str(w)
                else:
                    week_display = 'w' + self.yearShort + str(w)

                day = week + '-' + str(d)
                if 0 == d:
                    day_display = 'macro ' + week_display + '_' + str(7) + ' ['
                else:
                    day_display = 'macro ' + week_display + '_' + str(d) + ' ['

                print(day_display, file=tji)
                # The -1 and -%w pattern tells the parser to pick the Monday in that week
                r = datetime.datetime.strptime(day,"%Y-W%W-%w")
                logger.debug(str(r))
                year_month_day = str(r).split(' ')
                print('    ' + year_month_day[0], file=tji)
                print(']', file=tji)

        tji.close()


def main():
    g = WeekGenerator('2021')
    g.produce_weeks()

if __name__ == '__main__':
    main()
