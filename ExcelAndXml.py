 # encoding: utf-8
__qq__ = 283576530

import xlrd
import sys
import getopt

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#coding='utf-8'
import xlrd


def getPathFileName(path):
    tmp = path.split('/');
    return tmp[len(tmp) -1 ].split('.')[0];

def xlsToxmlPath(path):
    return path.split('.')[0] + '.xml';

def export(path):
    data = xlrd.open_workbook(path)
    table = data.sheets()[0]

    f = open(xlsToxmlPath(path), 'wb')
    f.write(u'<?xml version="1.0" encoding="utf-8" ?>\n')
    #f.write(u'<%s>\n' % getPathFileName(path))
    docType = int(table.cell(0, 0).value)
    if docType == 1 :
        firstRoot = str(table.cell(0, 1).value)
        secondRoot = str(table.cell(0, 2).value)

        f.write('<' + firstRoot+ '>' + '\n')
        for i in range(3, table.nrows):
            linestr = u'\t<' + secondRoot
            for j in range(0,table.ncols):
                colType = str(table.cell(2, j).value)
                if colType == 'string' :
                    linestr = linestr + u'\t' + table.cell(1, j).value + u'=' + u'"'+ str(table.cell(i, j).value) + u'"'
                else :
                    linestr = linestr + u'\t' + table.cell(1, j).value + u'=' + u'"'+ str(int(table.cell(i, j).value)) + u'"'                 
            linestr = linestr + u'/>'
            f.write(linestr)
            f.write('\n');
        f.write('</' + firstRoot + '>')

    elif docType == 2 :
        firstRoot = str(table.cell(0, 1).value)  
        f.write('<' + firstRoot+ '>' + '\n')
        rowLenNum = len(table.row(0))
        print(rowLenNum)
        for layerId in range(2,rowLenNum):
            print('layerId=' + str(layerId) )
            if str(table.cell(0, layerId).value) != "" :
                curRoot = str(table.cell(0, layerId).value)
                print(curRoot)
                beginRowId = 1 + (layerId-2)*3
                
                linestr = u'\t<' + curRoot
                for j in range(0,table.ncols):
                    if str(table.cell(beginRowId, j).value) != "" :
                        colType = str(table.cell(beginRowId+1, j).value)
                        print(beginRowId)
                        print(j)
                        print(colType)
                        if colType == 'string' :
                            linestr = linestr + u'\t' + table.cell(beginRowId, j).value + u'=' + u'"'+ str(table.cell(beginRowId+2, j).value) + u'"'
                        else :
                            linestr = linestr + u'\t' + table.cell(beginRowId, j).value + u'=' + u'"'+ str(int(table.cell(beginRowId+2, j).value)) + u'"'                 
                linestr = linestr + u'/>'
                f.write(linestr)
                f.write('\n');
                
        f.write('</' + firstRoot + '>')
#    else :

    #f.write(u'</%s>' % getPathFileName(path));
#export('E:/workspace/python/python/ExelToXML/mytest.xls')

if __name__ == '__main__':
    path =  sys.argv[1]
    export(path)
