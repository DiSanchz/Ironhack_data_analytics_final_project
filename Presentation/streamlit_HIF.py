### IMPORTS


from importfuncs import *
import streamlit as st
from streamlit_folium import folium_static


###########
#STREAMLIT
###########

st.header('Data-driven decision making for geospatial data: Airbnb in the Canary Islands')
#st.text('''Data analytics bootcamp - Final project''')

selectbox_1 = st.sidebar.selectbox("Choose your display style:",
    ("Selected locations", "Full hexmap - simple" , "Full hexmap - compound"))

###########
#Full hexmap - simple
###########

if selectbox_1 == "Full hexmap - simple":

    select2 = st.sidebar.selectbox('Filter type', ['General','Specific'] )

    if select2 == 'General':

        
        select3 = st.sidebar.selectbox('Spot-type of interest', ["All", "Natural attractions",
                                     "Cultural Atractions", "Golf", "Theme Parks", "Beaches", 
                                     "Transport", "Shopping"] )

        if select3 == 'All':
            listhex_chocie = listhex_allspots
        elif select3 == "Natural attractions":
            listhex_chocie = listhex_natural
        elif select3 == "Cultural Atractions":
            listhex_chocie = listhex_cultural
        elif select3 == "Golf":
            listhex_chocie = listhex_golf
        elif select3 == "Theme Parks":
            listhex_chocie = listhex_amuse
        elif select3 == "Beaches":
            listhex_chocie = listhex_beach
        elif select3 == "Transport":
            listhex_chocie = listhex_trans
        elif select3 == "Shopping":
            listhex_chocie = listhex_shop

        sample_hexmap = kamaz_cloro(listhex2= listhex_chocie, legend=False)
        folium_static(sample_hexmap)
    
    if select2 == 'Specific':
        
        select3 = st.sidebar.selectbox('Spot-type of interest', ["All", "Natural attractions",
                                     "Cultural Atractions", "Golf", "Theme Parks", "Beaches", 
                                     "Transport", "Shopping"] )

        if select3 == 'All':
            listhex_chocie = listhex_allspots
        elif select3 == "Natural attractions":
            listhex_chocie = listhex_natural
        elif select3 == "Cultural Atractions":
            listhex_chocie = listhex_cultural
        elif select3 == "Golf":
            listhex_chocie = listhex_golf
        elif select3 == "Theme Parks":
            listhex_chocie = listhex_amuse
        elif select3 == "Beaches":
            listhex_chocie = listhex_beach
        elif select3 == "Transport":
            listhex_chocie = listhex_trans
        elif select3 == "Shopping":
            listhex_chocie = listhex_shop

        slide1 = st.sidebar.slider("Nº of highlighted areas", 1,8)

        sample_hexmap2 = kamaz_cloro_ktop(listhex2 = listhex_chocie, legend=False, k = slide1 )
        folium_static(sample_hexmap2)


###########
#Full hexmap - compound
###########

if selectbox_1 == "Full hexmap - compound":

    slide665 = st.sidebar.selectbox("Nº of preferences", ['2','3','4'])

    if int(slide665) == 2:

        selecta = st.sidebar.selectbox('Spot-type of interest 1', ["All", "Natural attractions",
                                     "Cultural Atractions", "Golf", "Theme Parks", "Beaches", 
                                     "Transport", "Shopping"] )

        if selecta == 'All':
            listhex_chociea = listhex_allspots
        elif selecta == "Natural attractions":
            listhex_chociea = listhex_natural
        elif selecta == "Cultural Atractions":
            listhex_chociea = listhex_cultural
        elif selecta == "Golf":
            listhex_chociea = listhex_golf
        elif selecta == "Theme Parks":
            listhex_chociea = listhex_amuse
        elif selecta == "Beaches":
            listhex_chociea = listhex_beach
        elif selecta == "Transport":
            listhex_chociea = listhex_trans
        elif selecta == "Shopping":
            listhex_chociea = listhex_shop

        slide667 = st.sidebar.slider("Nº of spots to consider", 1,8)

        selectb = st.sidebar.selectbox('Spot-type of interest 2', ["All", "Natural attractions",
                                     "Cultural Atractions", "Golf", "Theme Parks", "Beaches", 
                                     "Transport", "Shopping"], key='mdfk' )

        if selectb == 'All':
            listhex_chocieb = listhex_allspots
        elif selectb == "Natural attractions":
            listhex_chocieb = listhex_natural
        elif selectb == "Cultural Atractions":
            listhex_chocieb = listhex_cultural
        elif selectb == "Golf":
            listhex_chocieb = listhex_golf
        elif selectb == "Theme Parks":
            listhex_chocieb = listhex_amuse
        elif selectb == "Beaches":
            listhex_chocieb = listhex_beach
        elif selectb == "Transport":
            listhex_chocieb = listhex_trans
        elif selectb == "Shopping":
            listhex_chocieb = listhex_shop

        slide668 = st.sidebar.slider("Nº of spots to consider", 1,8, key='mdfk2')

        sample_combmap2 = combo2(listhexa = listhex_chociea, listhexb = listhex_chocieb, ka = slide667, kb = slide668 )
        folium_static(sample_combmap2)

    
    elif int(slide665) == 3:


        selecta = st.sidebar.selectbox('Spot-type of interest 1', ["All", "Natural attractions",
                                     "Cultural Atractions", "Golf", "Theme Parks", "Beaches", 
                                     "Transport", "Shopping"], key = 'cambuyon' )

        if selecta == 'All':
            listhex_chociea = listhex_allspots
        elif selecta == "Natural attractions":
            listhex_chociea = listhex_natural
        elif selecta == "Cultural Atractions":
            listhex_chociea = listhex_cultural
        elif selecta == "Golf":
            listhex_chociea = listhex_golf
        elif selecta == "Theme Parks":
            listhex_chociea = listhex_amuse
        elif selecta == "Beaches":
            listhex_chociea = listhex_beach
        elif selecta == "Transport":
            listhex_chociea = listhex_trans
        elif selecta == "Shopping":
            listhex_chociea = listhex_shop

        slide667 = st.sidebar.slider("Nº of spots to consider", 1,8)

        selectb = st.sidebar.selectbox('Spot-type of interest 2', ["All", "Natural attractions",
                                     "Cultural Atractions", "Golf", "Theme Parks", "Beaches", 
                                     "Transport", "Shopping"], key='mdfkar' )

        if selectb == 'All':
            listhex_chocieb = listhex_allspots
        elif selectb == "Natural attractions":
            listhex_chocieb = listhex_natural
        elif selectb == "Cultural Atractions":
            listhex_chocieb = listhex_cultural
        elif selectb == "Golf":
            listhex_chocieb = listhex_golf
        elif selectb == "Theme Parks":
            listhex_chocieb = listhex_amuse
        elif selectb == "Beaches":
            listhex_chocieb = listhex_beach
        elif selectb == "Transport":
            listhex_chocieb = listhex_trans
        elif selectb == "Shopping":
            listhex_chocieb = listhex_shop

        slide668 = st.sidebar.slider("Nº of spots to consider", 1,8, key='mdfkrell')


        selectc = st.sidebar.selectbox('Spot-type of interest 3', ["All", "Natural attractions",
                                     "Cultural Atractions", "Golf", "Theme Parks", "Beaches", 
                                     "Transport", "Shopping"], key='mdfkare' )


        if selectc == 'All':
            listhex_chociec = listhex_allspots
        elif selectc == "Natural attractions":
            listhex_chociec = listhex_natural
        elif selectc == "Cultural Atractions":
            listhex_chociec = listhex_cultural
        elif selectc == "Golf":
            listhex_chociec = listhex_golf
        elif selectc == "Theme Parks":
            listhex_chociec = listhex_amuse
        elif selectc == "Beaches":
            listhex_chociec = listhex_beach
        elif selectc == "Transport":
            listhex_chociec = listhex_trans
        elif selectc == "Shopping":
            listhex_chociec = listhex_shop

        slide669 = st.sidebar.slider("Nº of spots to consider", 1,8, key='mdfking')

        sample_combmap3 = combo3(listhexa = listhex_chociea, listhexb = listhex_chocieb, listhexc = listhex_chociec,
         ka = slide667, kb = slide668, kc = slide669 )
        folium_static(sample_combmap3)


    elif int(slide665) == 4:


        selecta = st.sidebar.selectbox('Spot-type of interest 1', ["All", "Natural attractions",
                                     "Cultural Atractions", "Golf", "Theme Parks", "Beaches", 
                                     "Transport", "Shopping"], key = 'cambuyonk' )

        if selecta == 'All':
            listhex_chociea = listhex_allspots
        elif selecta == "Natural attractions":
            listhex_chociea = listhex_natural
        elif selecta == "Cultural Atractions":
            listhex_chociea = listhex_cultural
        elif selecta == "Golf":
            listhex_chociea = listhex_golf
        elif selecta == "Theme Parks":
            listhex_chociea = listhex_amuse
        elif selecta == "Beaches":
            listhex_chociea = listhex_beach
        elif selecta == "Transport":
            listhex_chociea = listhex_trans
        elif selecta == "Shopping":
            listhex_chociea = listhex_shop

        slide667 = st.sidebar.slider("Nº of spots to consider", 1,8)

        selectb = st.sidebar.selectbox('Spot-type of interest 2', ["All", "Natural attractions",
                                     "Cultural Atractions", "Golf", "Theme Parks", "Beaches", 
                                     "Transport", "Shopping"], key='mdfkark' )

        if selectb == 'All':
            listhex_chocieb = listhex_allspots
        elif selectb == "Natural attractions":
            listhex_chocieb = listhex_natural
        elif selectb == "Cultural Atractions":
            listhex_chocieb = listhex_cultural
        elif selectb == "Golf":
            listhex_chocieb = listhex_golf
        elif selectb == "Theme Parks":
            listhex_chocieb = listhex_amuse
        elif selectb == "Beaches":
            listhex_chocieb = listhex_beach
        elif selectb == "Transport":
            listhex_chocieb = listhex_trans
        elif selectb == "Shopping":
            listhex_chocieb = listhex_shop

        slide668 = st.sidebar.slider("Nº of highlighted areas", 1,8, key='mdfkrellp')


        selectc = st.sidebar.selectbox('Spot-type of interest 3', ["All", "Natural attractions",
                                     "Cultural Atractions", "Golf", "Theme Parks", "Beaches", 
                                     "Transport", "Shopping"], key='mdfkarep' )


        if selectc == 'All':
            listhex_chociec = listhex_allspots
        elif selectc == "Natural attractions":
            listhex_chociec = listhex_natural
        elif selectc == "Cultural Atractions":
            listhex_chociec = listhex_cultural
        elif selectc == "Golf":
            listhex_chociec = listhex_golf
        elif selectc == "Theme Parks":
            listhex_chociec = listhex_amuse
        elif selectc == "Beaches":
            listhex_chociec = listhex_beach
        elif selectc == "Transport":
            listhex_chociec = listhex_trans
        elif selectc == "Shopping":
            listhex_chociec = listhex_shop

        slide669 = st.sidebar.slider("Nº of spots to consider", 1,8, key='mdfkingoo')


        selectd = st.sidebar.selectbox('Spot-type of interest 4', ["All", "Natural attractions",
                                     "Cultural Atractions", "Golf", "Theme Parks", "Beaches", 
                                     "Transport", "Shopping"], key='mdfkareo' )


        if selectd == 'All':
            listhex_chocied = listhex_allspots
        elif selectd == "Natural attractions":
            listhex_chocied = listhex_natural
        elif selectd == "Cultural Atractions":
            listhex_chocied = listhex_cultural
        elif selectd == "Golf":
            listhex_chocied = listhex_golf
        elif selectd == "Theme Parks":
            listhex_chocied = listhex_amuse
        elif selectd == "Beaches":
            listhex_chocied = listhex_beach
        elif selectd == "Transport":
            listhex_chocied = listhex_trans
        elif selectd == "Shopping":
            listhex_chocied = listhex_shop

        slide670 = st.sidebar.slider("Nº of spots to consider", 1,8, key='mdfkingo')


        sample_combmap4 = combo4(listhexa = listhex_chociea, listhexb = listhex_chocieb, listhexc = listhex_chociec, listhexd = listhex_chocied,
         ka = slide667, kb = slide668, kc = slide669, kd = slide670 )
        folium_static(sample_combmap4)


###########
#Pinpoint
###########

elif selectbox_1 == "Selected locations":


    select1 = st.sidebar.selectbox("Distance mode:", ["near", "far"])
    select2 = st.sidebar.selectbox('Spot-type of interest', ["All", "Natural attractions",
                                     "Cultural Atractions", "Golf", "Theme Parks", "Beaches", 
                                     "Transport", "Shopping"] )
    
    if select2 == 'All':
        listhex_chocie = listhex_allspots
    elif select2 == "Natural attractions":
        listhex_chocie = listhex_natural
    elif select2 == "Cultural Atractions":
        listhex_chocie = listhex_cultural
    elif select2 == "Golf":
        listhex_chocie = listhex_golf
    elif select2 == "Theme Parks":
        listhex_chocie = listhex_amuse
    elif select2 == "Beaches":
        listhex_chocie = listhex_beach
    elif select2 == "Transport":
        listhex_chocie = listhex_trans
    elif select2 == "Shopping":
        listhex_chocie = listhex_shop

    slide1 = st.sidebar.slider("Nº of highlighted areas", 1,25)
    
    

    sample_hexmap = hex_pinpoint(listhex2 = listhex_chocie ,n=slide1, setting = select1)
    folium_static(sample_hexmap)
        
    








