'''
网页打开方法：
点击运行，将最后一行中括号前的内容复制到剪贴板，打开终端，输入python -m (粘贴剪贴板内容) 回车
streamlit表情大全：https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
'''

import streamlit as st
from PIL import Image
page=st.sidebar.radio("我的主页",["我的兴趣推荐","我的图片处理工具","我的智慧词典","我的留言区","我的音乐空间"])

def page1():
    '''我的兴趣推荐'''
    st.write("xnews爱骑行")
    st.image("riding.jpg",caption="和同学一起/姐会撒把嘿嘿嘿")
    st.write("--------------------")
    st.write("xnews不会刷题")
    st.image("school.jpg",caption="山东省实验中学")
    st.write("--------------------")
    st.write("xnews与天空")
    st.image("my_sky.jpg",caption="致力于收集全国各地的sky")
    
def page2():
    '''我的图片处理工具'''
    st.write("图片处理小程序")
    uploaded_file=st.file_uploader("放入你的图片",type=["png","jpeg","jpg"])
    st.write(":star2:处理1：图片RGB换色")
    if uploaded_file:
        file_name=uploaded_file.name
        file_type=uploaded_file.type
        file_size=uploaded_file.size
        img=Image.open(uploaded_file)
        tab1,tab2,tab3,tab4=st.tabs(["原图","改色1","改色2","改色3"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img,1,2,0))
        with tab3:
            st.image(img_change(img,0,2,1))
        with tab4:
            st.image(img_change(img,1,0,2))
    st.write(":star2:处理2：像素化")
    if uploaded_file:
        file_name=uploaded_file.name
        file_type=uploaded_file.type
        file_size=uploaded_file.size
        img=Image.open(uploaded_file)
        tab1,tab2,tab3,tab4=st.tabs(["原图","1/4","1/8","1/16"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_xiangsu(img,4))
        with tab3:
            st.image(img_xiangsu(img,8))
        with tab4:
            st.image(img_xiangsu(img,16))
            
    st.write(":star:处理3：缩放")
    if uploaded_file:
        file_name=uploaded_file.name
        file_type=uploaded_file.type
        file_size=uploaded_file.size
        img=Image.open(uploaded_file)
        img_width,img_height=img.size
        goal_w=st.number_input("要把图片的宽改为：",step=1,min_value=1)
        goal_h=st.number_input("要把图片的高改为：",min_value=1,step=1)
        tab1,tab2,tab3,tab4=st.tabs(["原图","缩放后","定宽等比例","定长等比例"])
        with tab1:
                st.image(img)
        try:
            with tab2:
                st.image(small_image(img,goal_w,goal_h))
            with tab3:
                st.image(small_image(img,goal_w,int(img_height/img_width*goal_w)))
            with tab4:
                st.image(small_image(img,int(img_width/img_height*goal_h),goal_h))
        except:
            pass
    
def page3():
    '''我的智慧词典'''
    st.write("xnews的智慧词典")
    with open("words_space.txt",'r',encoding='utf-8')as f:
        dictionary=f.read().split("\n")
    with open("check_out_times.txt",'r',encoding='utf-8')as f:
        times_list=f.read().split("\n")
    for i in range(len(dictionary)):
        dictionary[i]=dictionary[i].split("#")
    for i in range(len(times_list)):
        times_list[i]=times_list[i].split("#")
    words_dict={}
    times_dict={}
    for i in dictionary:
        words_dict[i[1]]=[int(i[0]),i[2]]
    for i in times_list:
        times_dict[int(i[0])]=int(i[1])
    word=st.text_input("请输入你要查询的单词：")
    if word in words_dict:
        st.write(words_dict[word][1])
        if word == 'python':
            st.code('''
                    #触发彩蛋！这是一行python代码
                    print("hello world!")''')#code可以直接输出代码格式
        if word=='birthday':
            st.balloons()
        if word=='snow':
            st.snow()
        if word=="newsqi":
            st.balloons()
            st.write(":ribbon:嘻嘻\n这是作者的名字奥")
        n=words_dict[word][0]
        if n in times_dict:
            times_dict[n]+=1
        else:
            times_dict[n]=1
        st.write("单词"+word+"已被查询"+str(times_dict[n])+"次")
        with open("check_out_times.txt",'w',encoding='utf=8') as f:
            message=''
            for k,v in times_dict.items():
                message+=str(k)+"#"+str(v)+"\n"
            message=message[:-1]
            f.write(message)
            
        
def page4():
    '''我的留言区'''
    with open("leave_message.txt","r",encoding='utf-8')as f:
        messages_list=f.read().split("\n")
    for i in range(len(messages_list)):
        messages_list[i]=messages_list[i].split("#")
    for i in messages_list:
        if i[1]=="小星":
            with st.chat_message("⭐"):
                st.write(str(i[1])+":"+str(i[2]))
        elif i[1]=="kiki":
            with st.chat_message("🎀"):
                st.write(str(i[1])+":"+str(i[2]))
    name=st.selectbox("你是___",["神秘人","小乐","小星","kiki"])
    new_message=st.text_input("请输入你的留言：")
    if st.button("留言"):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
        with open("leave_message.txt","w",encoding="utf-8")as f:
            message=""
            for i in messages_list:
                message+=i[0]+"#"+i[1]+"#"+i[2]+"\n"
            message=message[:-1]
            f.write(message)
        
    
    
def page5():
    '''我的音乐空间'''
    st.write("周深·璀璨冒险人")
    with open("璀璨冒险人.mp3","rb") as f:
        mymp3=f.read()
    st.audio(mymp3,format="audio/mp3",start_time=0)
    st.write("周深·借过一下")
    with open("借过一下.mp4","rb") as f:
        myvedio=f.read()
    st.video(myvedio,start_time=0)
    
def img_change(img,rc,gc,bc):#图片rgb换色
    width,height=img.size
    img_array=img.load()
    for x in range(width):
        for y in range(height):
            r=img_array[x,y][rc]
            g=img_array[x,y][gc]
            b=img_array[x,y][bc]
            img_array[x,y]=(r,g,b)
    return img
    
def img_xiangsu(img,num):
    width,height=img.size
    img_array=img.load()
    for x in range(width):
        for y in range(height):
            img_array[x,y]=img_array[x-x%num,y-y%num]
    return img
def small_image(img,w,h):
    newimage=img.resize((w,h))
    return newimage
    
if page=="我的兴趣推荐":
    page1()
elif page=="我的图片处理工具":
    page2()
elif page=="我的智慧词典":
    page3()
elif page=="我的留言区":
    page4()
elif page=="我的音乐空间":
    page5()