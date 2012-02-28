// ERPNext - web based ERP (http://erpnext.com)
// Copyright (C) 2012 Web Notes Technologies Pvt Ltd
// 
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
// 
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
// 
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.

report.customize_filters = function() {
  this.hide_all_filters();
  this.add_filter({fieldname:'show_group_balance', label:'Show Group Balance', fieldtype:'Select', options:NEWLINE+'Yes'+NEWLINE+'No',ignore : 1, parent:'Account'});
  this.add_filter({fieldname:'level', label:'Level', fieldtype:'Data', default:3,ignore : 1, parent:'Account'});
  
  this.add_filter({fieldname:'from_date', label:'Date', fieldtype:'Date', parent:'Account'});

  
  this.filter_fields_dict['Account'+FILTER_SEP +'Company'].df.filter_hide = 0;
  //this.filter_fields_dict['Account'+FILTER_SEP +'From Date'].df.filter_hide = 0;
  //this.filter_fields_dict['Account'+FILTER_SEP +'To Date'].df.filter_hide = 0;

  //this.large_report = 1;
}

report.aftertableprint = function(t) {
   $yt(t,'*',1,{whiteSpace:'pre'});
}