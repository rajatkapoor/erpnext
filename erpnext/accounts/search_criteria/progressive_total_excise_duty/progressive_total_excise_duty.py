# ERPNext - web based ERP (http://erpnext.com)
# Copyright (C) 2012 Web Notes Technologies Pvt Ltd
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Add columns
# -----------
row_list = [['Date', 'Date', '150px', '']
           ,['INVOICE', 'Date', '150px', '']
           ,['Baisc Excise Duty', 'Currency', '150px', '']
           ,['Education Cess', 'Currency', '150px', '']
           ,['S.H.Education Cess', 'Currency', '150px', '']
           ,['Remarks', 'Data', '150px', '']
]

for r in row_list:
  colnames.append(r[0])
  coltypes.append(r[1])
  colwidths.append(r[2])
  coloptions.append(r[3])
  col_idx[r[0]] = len(colnames)-1

# Get Object Of GL Control
#import webnotes
#import webnotes.model.code
#from webnotes.model.code import get_obj
#glc = webnotes.model.code.get_obj('GL Control')

# Get Year Start Date
ysd = sql("select year_start_date from `tabFiscal Year` where name='%s'" % filter_values['fiscal_year'])
ysd = ysd and ysd[0][0] or ''

# get as_on_date for opening
as_on_date = ''
if filter_values.get('posting_date'):
  as_on_date = add_days(filter_values['posting_date'], -1)

# Get Opening Balance
def get_opening_balance(acc, fy, as_on_date, ysd, get_opening_balance):
  #import webnotes
  #import webnotes.model.code
  #from webnotes.model.code import get_obj
  #glc = webnotes.model.code.get_obj('GL Control')
  glc = get_obj('GL Control')
  acc_det = sql("select debit_or_credit, is_pl_account, lft, rgt, group_or_ledger from tabAccount where name = '%s'" % acc)
  return glc.get_as_on_balance(acc, fy, as_on_date, acc_det[0][0], acc_det[0][2], acc_det[0][3])[2]

cum_sum_main_acc_head = cum_sum_add_acc_head = cum_sum_cvd_acc_head = cum_sum_edu_cess_acc_head = cum_sum_sh_edu_cess_acc_head = 0
openg_main_acc_head = openg_add_acc_head = openg_cvd_acc_head = openg_edu_cess_acc_head = openg_sh_edu_cess_acc_head = 0

# Get Opening of Basic Excise Duty
if not filter_values['main_acc_head']: 
  msgprint("Please Enter Main Account Head")
  raise Exception
cum_sum_main_acc_head = openg_main_acc_head = get_opening_balance(filter_values['main_acc_head'], filter_values['fiscal_year'], as_on_date, ysd, get_opening_balance)

# Get Opening of edu_cess_acc_head
if not filter_values['edu_cess_acc_head'] :
  msgprint("Please Enter Edu Cess Account Head")
  raise Exception
cum_sum_edu_cess_acc_head = openg_edu_cess_acc_head = get_opening_balance(filter_values['edu_cess_acc_head'], filter_values['fiscal_year'], as_on_date, ysd, get_opening_balance)

# Get Opening of sh_edu_cess_acc_head
if not filter_values['sh_edu_cess_acc_head'] :
  msgprint("Please Enter S.H.Edu Cess Account Head")
  raise Exception
cum_sum_sh_edu_cess_acc_head = openg_sh_edu_cess_acc_head = get_opening_balance(filter_values['sh_edu_cess_acc_head'], filter_values['fiscal_year'], as_on_date, ysd, get_opening_balance)

out = []

out.append(['Opening Balance of Duty in Credit', '', flt(openg_main_acc_head) + flt(openg_add_acc_head) , flt(openg_edu_cess_acc_head), flt(openg_sh_edu_cess_acc_head),''])
out += res
#if from_export == 0:
#  msgprint("This is a very large report and cannot be shown in the browser as it is likely to make your browser very slow.Please click on 'Export' to open in a spreadsheet")
#  raise Exception