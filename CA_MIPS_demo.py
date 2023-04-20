import tkinter as tk

from PIL import Image, ImageTk 
# 引入訊息視窗模組
import tkinter.messagebox
import re
optable=["add","sub","subu","addu","sll","srl","slt","sltu","and","or","nor","jr", #r type
     "addi","addiu","slti","lw","sw","beq","bne",  #i type
     "j","jal"] #j type
regtable={'$zero':'00000','$0':'00000',
          '$at':'00001','$1':'00001',
          '$v0':'00010','$2':'00010',
          '$v1':'00011','$3':'00011',
          '$a0':'00100','$4':'00100',
          '$a1':'00101','$5':'00101',
          '$a2':'00110','$6':'00110',
          '$a3':'00111','$7':'00111',
          '$t0':'01000','$8':'01000',
          '$t1':'01001','$9':'01001',
          '$t2':'01010','$10':'01010',
          '$t3':'01011','$11':'01011',
          '$t4':'01100','$12':'01100',
          '$t5':'01101','$13':'01101',
          '$t6':'01110','$14':'01110',
          '$t7':'01111','$15':'01111',
          '$s0':'10000','$16':'10000',
          '$s1':'10001','$17':'10001',
          '$s2':'10010','$18':'10010',
          '$s3':'10011','$19':'10011',
          '$s4':'10100','$20':'10100',
          '$s5':'10101','$21':'10101',
          '$s6':'10110','$22':'10110',
          '$s7':'10111','$23':'10111',
          '$t8':'11000','$24':'11000',
          '$t9':'11001','$25':'11001',
          '$k0':'11010','$26':'11010',
          '$k1':'11011','$27':'11011',
          '$gp':'11100','$28':'11100',
          '$sp':'11101','$29':'11101',
          '$fp':'11110','$30':'11110',
          '$ra':'11111','$31':'11111',
}

mips_optable = {
#     'R':{
     'add':'000000','sub':'000000','slt':'000000',
          'sll':'000000','SRL':'000000','and':'000000',
          'or':'000000','nor':'000000','addu':'000000',
          'jr':'000000','sltu':'000000',
     #    },
#     'I':{
     "addi":"001000","lw":"100011","sw":"101011","beq":"000100",
          "bne":"000101","addiu":"001001","slti":"001010",
     #    },
#     'J':{
     "j":"000010","jal":"000011"
     # }
}

mips_functable = {
     'add':'100000', 'sub':'100010', 'slt':'101010', 'sll':'000000','srl':'000010','and':'100100',
     'or':'100101','nor':'100111','addu':'100001','jr':'001000','sltu':'101011'

}

win = tk.Tk()  # 建立視窗
win.title("MIPS Test")
win.geometry("700x400+250+150")#大小+y+x
label = tk.Label(win, text = 'Please Enter MIPS instruction:',
          font = ('Arial', 15))

label.pack() #顯示



entry = tk.Entry(win, width = 20) # 輸入欄位的寬度
entry.pack()
instruction_operands = tk.Label(font = ('Arial', 15)) #顯示operands
instruction_operation = tk.Label(font = ('Arial', 15)) #顯示operation
instruction_destination = tk.Label(font = ('Arial', 15))
instruction_source1 = tk.Label(font = ('Arial', 15))
instruction_source2 = tk.Label(font = ('Arial', 15))
instruction_imm = tk.Label(font = ('Arial', 15))
instruction_memery = tk.Label(font = ('Arial', 15))
# errormsg_text = tk.Label(font = ('Arial', 15))

instruction_opcode = tk.Label(font = ('Arial', 15))
instruction_rd = tk.Label(font = ('Arial', 15))
instruction_rs = tk.Label(font = ('Arial', 15))
instruction_rt = tk.Label(font = ('Arial', 15))
instruction_shamt_b= tk.Label(font = ('Arial', 15))
instruction_func_b= tk.Label(font = ('Arial', 15))
instruction_imm_b= tk.Label(font = ('Arial', 15))
instruction_address = tk.Label(font = ('Arial', 15))

def identify():
     init_sentence = entry.get()
     sentence = init_sentence.replace(",","")#用replace扣除掉指令的逗號
     token=sentence.split(" ")#將指令分割，所以指令一定要打", "空格
     operation = token[0] #指令類別
     pattern = re.compile('[0-9]+')
     num = pattern.findall(sentence)#全部的數字們陣列
     # if token[0] != options[0:len(options)-1]:
     if operation not in optable:#判斷指令是否存在
          tkinter.messagebox.showinfo(title = 'alert', # 視窗標題
                                   message = 'operations not inside!')   # 訊息內容
     else:
          if(token[0]=='add' or token[0]=='sub'or token[0]=='addu'or token[0]=='subu' or token[0]=='mul'
               or token[0]=='slt' or token[0]=='sltu' or token[0]=='and'or token[0]=='or'or token[0]=='nor'):#記得要or整串不能只or字的部分

               if (token[1][0]!='$'or token[2][0]!='$'or token[3][0]!='$'): #沒有
                    tkinter.messagebox.showinfo(title = 'alert', # 視窗標題
                                        message = 'register error')   # 訊息內容
               elif(len(token) != 4):
                    tkinter.messagebox.showinfo(title = 'alert', # 視窗標題
                                        message = 'incorrect length of instruction')   # 訊息內容
               elif(int(num[0]) >31 or int(num[1]) >31 or int(num[2]) >31):
                    tkinter.messagebox.showinfo(title = 'alert', # 視窗標題
                                        message = 'register number out of range')   # 訊息內容
               else:
                    operation_text = 'operation: '+token[0]
                    destination_text='destination: '+token[1]
                    source1_text='source1: '+token[2]
                    source2_text='source2: '+token[3]
                    instruction_operation.config(text=operation_text)
                    instruction_destination.config(text=destination_text)
                    instruction_source1.config(text=source1_text)
                    instruction_source2.config(text=source2_text)

                    instruction_opcode_text = 'op: '+ str(mips_optable[token[0]])
                    instruction_rd_text = 'rd: ' + regtable[str(token[1])]
                    instruction_rs_text = 'rs: ' + regtable[str(token[2])]
                    instruction_rt_text = 'rt: ' + regtable[str(token[3])]
                    instruction_shamt_b_text = 'shamt: 00000'
                    instruction_func_b_text = 'func: '+mips_functable[token[0]]

                    instruction_opcode.config(text=instruction_opcode_text)
                    instruction_rd.config(text=instruction_rd_text)
                    instruction_rs.config(text=instruction_rs_text)
                    instruction_rt.config(text=instruction_rt_text)
                    instruction_shamt_b.config(text = instruction_shamt_b_text)
                    instruction_func_b.config(text=instruction_func_b_text)


          elif(token[0]=='jr'):
               if(len(token) != 2):
                    tkinter.messagebox.showinfo(title = 'alert', # 視窗標題
                                        message = 'incorrect length of instruction')   # 訊息內容
               elif (token[1][0]!='$'):
                    tkinter.messagebox.showinfo(title = 'alert', # 視窗標題
                                        message = 'register error')
               elif(int(num[0]) >31):
                    tkinter.messagebox.showinfo(title = 'alert', # 視窗標題
                                        message = 'register number out of range')   # 訊息內容
               else:
                    operation_text = 'operation: '+token[0]
                    destination_text='source: '+token[1]
                    instruction_operation.config(text=operation_text)
                    instruction_destination.config(text=destination_text) 
                    instruction_source1.config(text='')
                    instruction_source2.config(text='')  

                    instruction_opcode_text = 'op: '+ str(mips_optable[token[0]])
                    instruction_rd_text = 'rd: 00000'
                    instruction_rs_text = 'rs: ' + regtable[str(token[1])]
                    instruction_rt_text = 'rt: 00000'
                    instruction_shamt_b_text = 'shamt: 00000'
                    instruction_func_b_text = 'func: '+mips_functable[token[0]]

                    instruction_opcode.config(text=instruction_opcode_text)
                    instruction_rd.config(text=instruction_rd_text)
                    instruction_rs.config(text=instruction_rs_text)
                    instruction_rt.config(text=instruction_rt_text)
                    instruction_shamt_b.config(text = instruction_shamt_b_text)
                    instruction_func_b.config(text=instruction_func_b_text)
                    
          elif(token[0]=='sll'or token[0]=='srl'):
               errormsg = list("")
               if (token[1][0]!='$' or token[2][0]!='$'):
                    # errormsg.append(str("register error! "))
                    tkinter.messagebox.showinfo(title = 'alert', # 視窗標題
                                        message = 'register error')
               elif(token[3].isdigit() !=1):
                    # errormsg.append(str("shamt error! "))
                    tkinter.messagebox.showinfo(title = 'alert', # 視窗標題
                                        message = 'shamt error')
               elif(token[1][2].isdigit() !=1 or token[2][2].isdigit() !=1):
                    # errormsg.append(str("register error! "))
                    tkinter.messagebox.showinfo(title = 'alert', # 視窗標題
                                        message = 'register error')
               elif(len(token) != 4):
                    # errormsg.append(str("incorrect length of instruction! "))
                    tkinter.messagebox.showinfo(title = 'alert', # 視窗標題
                                        message = 'incorrect length of instruction')   # 訊息內容
               elif(int(num[0]) >31 or int(num[1]) >31):
                    # errormsg.append(str("register number out of range! "))
                    tkinter.messagebox.showinfo(title = 'alert', # 視窗標題
                                        message = 'register number out of range')   # 訊息內容
               elif(int(num[2]) >31 or int(num[2]) < 0 or token[3].isdigit()== False): #shamt需大於0小於32且為立即值
                    # errormsg.append(str("shamt number out of range! "))
                    tkinter.messagebox.showinfo(title = 'alert', # 視窗標題
                                        message = 'shamt number out of range')
               elif(len(errormsg) != 0):
                    # errormsg_text.config(text = errormsg)
                    tkinter.messagebox.showinfo(title = 'alert', # 視窗標題
                                        message = str(errormsg))
               else:
                    operation_text = 'operation: '+token[0]
                    destination_text='destination: '+token[1]
                    source1_text='source1: '+token[2]
                    source2_text='source2: '+token[3]
                    instruction_operation.config(text=operation_text)
                    instruction_destination.config(text=destination_text)
                    instruction_source1.config(text=source1_text)
                    instruction_source2.config(text=source2_text)
                    # errormsg_text.config(text = errormsg)

                    instruction_opcode_text = 'op: '+ str(mips_optable[token[0]])
                    instruction_rd_text = 'rd: ' + regtable[str(token[1])]
                    instruction_rs_text = 'rs: 00000'
                    instruction_rt_text = 'rt: ' + regtable[str(token[2])]
                    pre_shamtnum = "{0:b}".format(int(token[3]))
                    shamtnum = pre_shamtnum.zfill(5)
                    instruction_shamt_b_text = 'shamt: ' + str(shamtnum)
                    instruction_func_b_text = 'func'+ mips_functable[token[0]]

                    instruction_opcode.config(text=instruction_opcode_text)
                    instruction_rd.config(text=instruction_rd_text)
                    instruction_rs.config(text=instruction_rs_text)
                    instruction_rt.config(text=instruction_rt_text)
                    instruction_shamt_b.config(text = instruction_shamt_b_text)
                    instruction_func_b.config(text=instruction_func_b_text)


          elif(token[0]=='addi' or token[0]=='addiu'):
               if (token[1][0]!='$' or token[2][0]!='$'):
                    tkinter.messagebox.showinfo(title = 'alert', # 視窗標題
                                        message = 'register error')
               elif(len(token) != 4):
                    tkinter.messagebox.showinfo(title = 'alert', # 視窗標題
                                        message = 'incorrect length of instruction')   # 訊息內容
               elif(int(num[0]) >31 or int(num[1]) >31):
                    tkinter.messagebox.showinfo(title = 'alert', # 視窗標題
                                        message = 'register number out of range')   # 訊息內容
               elif(int(num[2]) < (-32768) or int(num[2]) > 32767):
                    tkinter.messagebox.showinfo(title = 'alert', # 視窗標題
                                        message = 'immediate value out of range')   # 訊息內容
               else:
                    operation_text = 'operation: '+token[0]
                    destination_text='destination: '+token[1]
                    source1_text='source: '+token[2]
                    source2_text='immediate value: '+token[3]
                    instruction_operation.config(text=operation_text)
                    instruction_destination.config(text=destination_text)
                    instruction_source1.config(text=source1_text)
                    instruction_source2.config(text=source2_text)

                    instruction_opcode_text = 'op: '+ str(mips_optable[token[0]])
                    instruction_rs_text = 'rs: '+ regtable[str(token[2])]
                    instruction_rt_text = 'rt: ' + regtable[str(token[1])]
                    pre_imm="{0:b}".format(int(token[3]))
                    imm = pre_imm.zfill(16)
                    instruction_imm_b_text = 'immVal: '+str(imm)


                    instruction_opcode.config(text=instruction_opcode_text)
                    instruction_rs.config(text=instruction_rs_text)
                    instruction_rt.config(text=instruction_rt_text)
                    instruction_imm_b.config(text=instruction_imm_b_text)

          elif(token[0]=='lw'):
               pre_sentence = sentence.replace("("," ")
               reg_sentence = pre_sentence.replace(")","")
               reg_token = reg_sentence.split(" ")
               #分割完會像是：'lw', '$8,', '3276', '$s0'

               if(len(reg_token) != 4): #offset要為4的倍數
                    tkinter.messagebox.showinfo(title = 'alert', # 視窗標題
                                        message = 'incorrect length of instruction')   # 訊息內容
               else:#長度為四的情況
                    if(reg_token[1][0] != '$'):
                         tkinter.messagebox.showinfo(title = 'alert', # 視窗標題
                                        message = 'wrong type of register')   # 訊息內容

                    elif(reg_token[2].isdigit() != 1 or (int(num[1]) %4) !=0): #判斷第二位是不是正整數 or (num[1] %4) !=0
                         tkinter.messagebox.showinfo(title = 'alert', # 視窗標題
                                        message = 'wrong type of offset')   # 訊息內容
                                        
                    elif(int(num[0]) >31 or int(num[2]) >31):
                         tkinter.messagebox.showinfo(title = 'alert', # 視窗標題
                                        message = 'register number out of range')   # 訊息內容
                    elif(int(num[1]) < (0) or int(num[1]) > 65535):
                         tkinter.messagebox.showinfo(title = 'alert', # 視窗標題
                                        message = 'offset value out of range')   # 訊息內容
                    else:
                         operation_text = 'operation: '+ reg_token[0]
                         destination_text='memery address: MEM['+ reg_token[3]+'+'+reg_token[2]+']'
                         source1_text='source: '+ reg_token[3]
                         source2_text='destination: '+reg_token[1]
                         instruction_operation.config(text=operation_text)
                         instruction_destination.config(text=destination_text)
                         instruction_source1.config(text=source1_text)
                         instruction_source2.config(text=source2_text)

                         instruction_opcode_text = 'op: '+ str(mips_optable[token[0]])
                         instruction_rs_text = 'rs: '+ regtable[str(reg_token[1])]
                         instruction_rt_text = 'rt: ' + regtable[str(reg_token[3])]
                         pre_imm="{0:b}".format(int(reg_token[2]))
                         imm = pre_imm.zfill(16)
                         instruction_imm_b_text = 'immVal: '+str(imm)


                         instruction_opcode.config(text=instruction_opcode_text)
                         instruction_rs.config(text=instruction_rs_text)
                         instruction_rt.config(text=instruction_rt_text)
                         instruction_imm_b.config(text=instruction_imm_b_text)



          elif(token[0] == 'sw'):
               pre_sentence = sentence.replace("("," ")
               reg_sentence = pre_sentence.replace(")","")
               reg_token = reg_sentence.split(" ")
               #分割完會像是：'lw', '$8,', '3276', '$s0'

               if(len(reg_token) != 4): #offset要為4的倍數
                    tkinter.messagebox.showinfo(title = 'alert', # 視窗標題
                                        message = 'incorrect length of instruction')   # 訊息內容
               else:#長度為四的情況
                    if(reg_token[1][0] != '$'):
                         tkinter.messagebox.showinfo(title = 'alert', # 視窗標題
                                        message = 'wrong type of register')   # 訊息內容

                    elif(reg_token[2].isdigit() != 1 or (int(num[1]) %4) !=0): #判斷第二位是不是正整數 or (num[1] %4) !=0
                         tkinter.messagebox.showinfo(title = 'alert', # 視窗標題
                                        message = 'wrong type of offset')   # 訊息內容
                                        
                    elif((token[1] not in regtable) or(token[3] not in regtable)):
                         tkinter.messagebox.showinfo(title = 'alert', # 視窗標題
                                        message = 'register number out of range')   # 訊息內容
                    elif(int(num[1]) < (0) or int(num[1]) > 65535):
                         tkinter.messagebox.showinfo(title = 'alert', # 視窗標題
                                        message = 'offset value out of range')   # 訊息內容
                    else:
                         operation_text = 'operation: '+ reg_token[0]
                         destination_text='memery address: MEM['+ reg_token[3]+'+'+reg_token[2]+']'
                         source1_text='source: '+ reg_token[1]
                         source2_text='destination: '+reg_token[3]
                         instruction_operation.config(text=operation_text)
                         instruction_destination.config(text=destination_text)
                         instruction_source1.config(text=source1_text)
                         instruction_source2.config(text=source2_text)

                         instruction_opcode_text = 'op: '+ str(mips_optable[token[0]])
                         instruction_rs_text = 'rs: '+ regtable[str(reg_token[1])]
                         instruction_rt_text = 'rt: ' + regtable[str(reg_token[3])]
                         pre_imm="{0:b}".format(int(reg_token[2]))
                         imm = pre_imm.zfill(16)
                         instruction_imm_b_text = 'immVal: '+str(imm)


                         instruction_opcode.config(text=instruction_opcode_text)
                         instruction_rs.config(text=instruction_rs_text)
                         instruction_rt.config(text=instruction_rt_text)
                         instruction_imm_b.config(text=instruction_imm_b_text)


          elif(token[0]=='beq' or token[0]=='bne'):                
               if (token[1][0]!='$' or token[2][0]!='$'):
                    tkinter.messagebox.showinfo(title = 'alert', # 視窗標題
                                        message = 'register error')
               elif((token[1] not in regtable)):
                    tkinter.messagebox.showinfo(title = 'alert', # 視窗標題
                                        message = 'cannot find register')
               elif((token[2] not in regtable)):
                    tkinter.messagebox.showinfo(title = 'alert', # 視窗標題
                                        message = 'cannot find register')
               elif(len(token) != 4):
                    tkinter.messagebox.showinfo(title = 'alert', # 視窗標題
                                        message = 'incorrect length of instruction')   # 訊息內容
          
               # elif(int(token[3]) < 0 ):
               #      token[3] = 
                    
               
               else:
                    operation_text = 'operation: '+token[0]
                    destination_text='source1: '+token[1]
                    source1_text='source2: '+token[2]
                    source2_text='address: '+token[3]
                    instruction_operation.config(text=operation_text)
                    instruction_destination.config(text=destination_text)
                    instruction_source1.config(text=source1_text)
                    instruction_source2.config(text=source2_text)

                    instruction_opcode_text = 'op: '+ str(mips_optable[token[0]])
                    instruction_rs_text = 'rs: '+ regtable[str(token[1])]
                    instruction_rt_text = 'rt: ' + regtable[str(token[2])]
                    pre_address="{0:b}".format(int(token[3])*4)
                    address = pre_address.zfill(16)
                    # edaddress="{0:b}".format((1111111111111111 or address) +1)
                    instruction_address_text = 'address: '+str(address)


                    instruction_opcode.config(text=instruction_opcode_text)
                    instruction_rs.config(text=instruction_rs_text)
                    instruction_rt.config(text=instruction_rt_text)
                    instruction_address.config(text=instruction_address_text)
          #elif(token[0]=='slti'):

          elif(token[0]=='j' or token[0]=='jal'):
               if(len(token) != 2):
                    tkinter.messagebox.showinfo(title = 'alert', # 視窗標題
                                        message = 'incorrect length of instruction')   # 訊息內容
               elif(token[1].isdigit() != 1):
                    tkinter.messagebox.showinfo(title = 'alert', # 視窗標題
                                        message = 'incorrect value of address')   # 訊息內容
               elif(int(token[1]) %4 != 0):
                    tkinter.messagebox.showinfo(title = 'alert', # 視窗標題
                                        message = 'address cannot divided by 4')   # 訊息內容
               else:
                    operation_text = 'operation: '+token[0]
                    destination_text='address: '+token[1]
                    instruction_operation.config(text=operation_text)
                    instruction_destination.config(text=destination_text)
                    instruction_source1.config(text='')
                    instruction_source2.config(text='')
                    
                    instruction_opcode_text = 'op: '+ str(mips_optable[token[0]])
                    pre_address="{0:b}".format(int(int(token[1])/4))
                    address = pre_address.zfill(26)
                    instruction_address_text = 'address: '+str(address)


                    instruction_opcode.config(text=instruction_opcode_text)
                    instruction_address.config(text=instruction_address_text)






# 按鈕
button = tk.Button(win, text = "OK", command = identify )
button.pack()
instruction_operation.pack()
instruction_destination.pack()
instruction_source1.pack()
instruction_source2.pack()
# errormsg_text.pack()

instruction_opcode.pack()
instruction_rd.pack()
instruction_rs.pack()
instruction_rt.pack()
instruction_shamt_b.pack()
instruction_func_b.pack()
instruction_imm_b.pack()
instruction_address.pack()


win.mainloop()# 不斷執行的意思 像是視窗要一直開

