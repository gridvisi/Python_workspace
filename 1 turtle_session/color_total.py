'''
x：指定要绘制直方图的数据；
bins：指定直方图条形的个数；
range：指定直方图数据的上下界，默认包含绘图数据的最大值和最小值；
normed：是否将直方图的频数转换成频率；
weights：该参数可为每一个数据点设置权重；
cumulative：是否需要计算累计频数或频率；
bottom：可以为直方图的每个条形添加基准线，默认为0；
histtype：指定直方图的类型，默认为bar，除此还有’barstacked’,‘step’, ‘stepfilled’；
align：设置条形边界值的对其方式，默认为mid，除此还有’left’和’right’；
orientation：设置直方图的摆放方向，默认为垂直方向；
rwidth：设置直方图条形宽度的百分比；
log：是否需要对绘图数据进行log变换；
color：设置直方图的填充色；
label：设置直方图的标签，可通过legend展示其图例；
stacked：当有多个数据时，是否需要将直方图呈堆叠摆放，默认水平摆放；

'''

c = [
'lightcoral',
'coral',
'darkorange',
'gold',
'palegreen',
'paleturquoise',
'skyblue',
'plum',
'hotpink',
'pink']


# program taken from http://stackoverflow.com/questions/4969543/colour-chart-for-tkinter-and-tix-using-python
#
from tkinter import *

MAX_ROWS = 36
FONT_SIZE = 10  # (pixels)

COLORS = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
          'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
          'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
          'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
          'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
          'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue', 'blue',
          'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
          'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
          'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
          'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
          'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
          'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
          'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
          'indian red', 'saddle brown', 'sandy brown',
          'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
          'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
          'pale violet red', 'maroon', 'medium violet red', 'violet red',
          'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
          'thistle', 'snow2', 'snow3',
          'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
          'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
          'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
          'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
          'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
          'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
          'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
          'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
          'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
          'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
          'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
          'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
          'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
          'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
          'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
          'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
          'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
          'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
          'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
          'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
          'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
          'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
          'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
          'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
          'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
          'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
          'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
          'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
          'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
          'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
          'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
          'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
          'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
          'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
          'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
          'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
          'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
          'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
          'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
          'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
          'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
          'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
          'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
          'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
          'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
          'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
          'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
          'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
          'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
          'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
          'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
          'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
          'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
          'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
          'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
          'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
          'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']

root = Tk()
root.title("Named colour chart")
row = 0
col = 0
for color in COLORS:
    e = Label(root, text=color, background=color,
              font=(None, -FONT_SIZE))
    e.grid(row=row, column=col, sticky=E + W)
    row += 1
    if (row > 36):
        row = 0
        col += 1

root.mainloop()


'''
Adobe Devanagari                   Agency FB                          
Algerian                           Arial                              Arial Rounded MT Bold              Arial Unicode MS                   
Baskerville Old Face               Bauhaus 93                         Bell MT                            Berlin Sans FB                     
Berlin Sans FB Demi                Bernard MT Condensed               Blackadder ITC                     Bodoni MT                          
Book Antiqua                       Bookman Old Style                  Bookshelf Symbol 7                 Bradley Hand ITC                   
Britannic Bold                     Broadway                           Brush Script MT                    Calibri                            
Californian FB                     Calisto MT                         Cambria                            Candara                            
Castellar                          Centaur                            Century                            Century Gothic                     
Century Schoolbook                 Chiller                            Colonna MT                         Comic Sans MS                      
Consolas                           Constantia                         Cooper Black                       Copperplate Gothic Bold            
Copperplate Gothic Light           Corbel                             Courier New                        Curlz MT                           
DejaVu Sans                        DejaVu Sans Display                DejaVu Sans Mono                   DejaVu Serif                       
DejaVu Serif Display               DengXian                           ESRI AMFM Electric                 ESRI AMFM Gas                      
ESRI AMFM Sewer                    ESRI AMFM Water                    ESRI ArcPad                        ESRI Arrowhead                     
ESRI Business                      ESRI Cartography                   ESRI Caves 1                       ESRI Caves 2                       
ESRI Caves 3                       ESRI Climate & Precipitation       ESRI Commodities                   ESRI Conservation                  
ESRI Crime Analysis                ESRI Default Marker                ESRI Dimensioning                  ESRI ERS Infrastructures S1        
ESRI ERS Operations S1             ESRI Elements                      ESRI Enviro Hazard Analysis        ESRI Enviro Hazard Incident        
ESRI Enviro Hazard Sites           ESRI Environmental & Icons         ESRI Fire Incident NFPA            ESRI Geology                       
ESRI Geology AGSO 1                ESRI Geology USGS 95-525           ESRI Geometric Symbols             ESRI Hazardous Materials           
ESRI Hydrants                      ESRI IGL Font16                    ESRI IGL Font20                    ESRI IGL Font21                    
ESRI IGL Font22                    ESRI IGL Font23                    ESRI IGL Font24                    ESRI IGL Font25                    
ESRI Meteorological 01             ESRI Mil2525C Modifiers            ESRI MilMod 01                     ESRI MilMod 02                     
ESRI MilRed 01                     ESRI MilSym 01                     ESRI MilSym 02                     ESRI MilSym 03                     
ESRI MilSym 04                     ESRI MilSym 05                     ESRI NIMA City Graphic LN          ESRI NIMA City Graphic PT          
ESRI NIMA DNC LN                   ESRI NIMA DNC PT                   ESRI NIMA VMAP1&2 LN               ESRI NIMA VMAP1&2 PT               
ESRI North                         ESRI Oil, Gas, & Water             ESRI Ordnance Survey               ESRI Pipeline US 1                 
ESRI Public1                       ESRI SDS 1.95 1                    ESRI SDS 1.95 2                    ESRI SDS 2.00 1                    
ESRI SDS 2.00 2                    ESRI Shields                       ESRI Surveyor                      ESRI Telecom                       
ESRI Transportation & Civic        ESRI US Forestry 1                 ESRI US Forestry 2                 ESRI US MUTCD 1                    
ESRI US MUTCD 2                    ESRI US MUTCD 3                    ESRI Weather                       Ebrima                             
Edwardian Script ITC               Elephant                           Engravers MT                       Eras Bold ITC                      
Eras Demi ITC                      Eras Light ITC                     Eras Medium ITC                    Euclid                             
Euclid Extra                       Euclid Fraktur                     Euclid Math One                    Euclid Math Two                    
Euclid Symbol                      FZCuHeiSongS-B-GB                  FZLanTingHeiS-UL-GB                FZShuTi                            
FZYaoTi                            FangSong                           Felix Titling                      Fences                             
Footlight MT Light                 Forte                              Franklin Gothic Book               Franklin Gothic Demi               
Franklin Gothic Demi Cond          Franklin Gothic Heavy              Franklin Gothic Medium             Franklin Gothic Medium Cond        
Freestyle Script                   French Script MT                   Gabriola                           Gadugi                             
Garamond                           Georgia                            Gigi                               Gill Sans MT                       
Gill Sans MT Condensed             Gill Sans MT Ext Condensed Bold    Gill Sans Ultra Bold               Gill Sans Ultra Bold Condensed     
Gloucester MT Extra Condensed      Goudy Old Style                    Goudy Stout                        Haettenschweiler                   
Harlow Solid Italic                Harrington                         High Tower Text                    HoloLens MDL2 Assets               
Impact                             Imprint MT Shadow                  Informal Roman                     Javanese Text                      
Jokerman                           Juice ITC                          KaiTi                              Kristen ITC                        
Kunstler Script                    Leelawadee                         Leelawadee UI                      LiSu                               
Lucida Bright                      Lucida Calligraphy                 Lucida Console                     Lucida Fax                         
Lucida Handwriting                 Lucida Sans                        Lucida Sans Typewriter             Lucida Sans Unicode                
MS Gothic                          MS Outlook                         MS Reference Sans Serif            MS Reference Specialty             
MT Extra                           MT Extra Tiger                     MV Boli                            Magneto                            
Maiandra GD                        Malgun Gothic                      Marlett                            Matura MT Script Capitals          
Meiryo                             Microsoft Himalaya                 Microsoft JhengHei                 Microsoft MHei                     
Microsoft NeoGothic                Microsoft New Tai Lue              Microsoft PhagsPa                  Microsoft Sans Serif               
Microsoft Tai Le                   Microsoft Uighur                   Microsoft YaHei                    Microsoft Yi Baiti                 
MingLiU-ExtB                       Mistral                            Modern No. 20                      Mongolian Baiti                    
Monotype Corsiva                   Myanmar Text                       Niagara Engraved                   Niagara Solid                      
Nirmala UI                         NumberOnly                         OCR A Extended                     Old English Text MT                
Onyx                               OriginGISSymbols                   Palace Script MT                   Palatino Linotype                  
Papyrus                            Parchment                          Perpetua                           Perpetua Titling MT                
Playbill                           Poor Richard                       Pristina                           Rage Italic                        
Ravie                              Rockwell                           Rockwell Condensed                 Rockwell Extra Bold                
STCaiyun                           STFangsong                         STHupo                             STIXGeneral                        
STIXNonUnicode                     STIXSizeFiveSym                    STIXSizeFourSym                    STIXSizeOneSym                     
STIXSizeThreeSym                   STIXSizeTwoSym                     STKaiti                            STLiti                             
STSong                             STXihei                            STXingkai                          STXinwei                           
STZhongsong                        Script MT Bold                     Segoe MDL2 Assets                  Segoe Print                        
Segoe Script                       Segoe UI                           Segoe UI Emoji                     Segoe UI Historic                  
Segoe UI Symbol                    Segoe WP                           Showcard Gothic                    SimHei                             
SimSun                             SimSun-ExtB                        Sitka Small                        Snap ITC                           
Stencil                            Sylfaen                            Symbol                             Symbol Tiger                       
Symbol Tiger Expert                Tahoma                             Tempus Sans ITC                    Tiger                              
Tiger Expert                       Times New Roman                    Trebuchet MS                       Tw Cen MT                          
Tw Cen MT Condensed                Tw Cen MT Condensed Extra Bold     Verdana                            Viner Hand ITC                     
Vivaldi                            Vladimir Script                    Webdings                           Wide Latin                         
Wingdings                          Wingdings 2                        Wingdings 3                        YouYuan                            
Yu Gothic                          ZWAdobeF                           cmb10                              cmex10                             
cmmi10                             cmr10                              cmss10                             cmsy10                             
cmtt10                             hakuyoxingshu7000                  icomoon  


'''