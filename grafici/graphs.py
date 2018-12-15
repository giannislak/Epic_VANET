
import matplotlib.pyplot as plt



# LUXEMBURG 50 NO OUTLIERS
forwarder_raw = [(50, 575.725), (60, 550.75), (70, 500.775), (80, 468.625), (90, 449.0), (100, 407.25), (110, 401.875), (120, 355.375), (130, 344.175), (140, 320.475), (150, 311.6), (160, 298.975), (170, 262.375), (180, 252.225), (190, 218.85), (200, 212.175), (210, 184.675), (220, 178.8), (230, 156.5), (240, 136.525), (250, 116.45), (260, 112.7), (270, 82.325), (280, 87.85), (290, 62.175), (300, 62.725), (310, 48.15), (320, 43.85), (330, 35.2), (340, 34.05)]
frw_r = [x[0] for x in forwarder_raw]
frw_n = [100*x[1]/802 for x in forwarder_raw]

#rmin = [50, 75, 100, 125, 150, 175, 200, 225, 250]
#frw = [602.5, 458.5, 431.3, 343, 333.5, 284, 256.2, 209.3, 146.9]
#plt.plot(frw_r, frw_n, 'r--')
#title = "Number of forwarders vs rmin")
#plt.title(title)
#plt.savefig(title+'.png')
#plt.clf()


recv_raw = [(50, 787.2307692307693), (60, 786.35), (70, 785.2894736842105), (80, 783.575), (90, 779.45), (100, 776.675), (110, 774.5384615384615), (120, 771.95), (130, 768.675), (140, 764.7948717948718), (150, 763.0512820512821), (160, 758.4857142857143), (170, 748.8333333333334), (180, 739.3076923076923), (190, 718.5263157894736), (200, 705.5897435897435), (210, 677.9714285714285), (220, 666.3157894736842), (230, 657.8888888888889), (240, 626.8947368421053), (250, 611.6944444444445), (260, 595.6875), (270, 566.2666666666667), (280, 505.27272727272725), (290, 480.0882352941176), (300, 468.64285714285717), (310, 418.09375), (320, 381.3703703703704), (330, 308.8888888888889), (340, 261.81481481481484)]
recv_r = [x[0] for x in recv_raw]
recv_n = [100*x[1]/802 for x in recv_raw]

plt.plot(frw_r, frw_n, 'r--', label='forwarders')
plt.plot(recv_r, recv_n, 'b--', label='receivers')
plt.ylim(0,100)
plt.legend(loc='upper right')
plt.xlabel('Rmin, m')
plt.ylabel('% total nodes')
title = "LUXEMBURG 50: %receivers (blue) forwaredrs (red) vs rmin NO OUTLIERS"
#plt.title(title)
plt.savefig(title+'.png')
plt.clf()



# LUXEMBURG 50 WITH OUTLIERS
raw = [(50, 562.075, 0.9329800498753117), (60, 550.025, 0.9803304239401496), (70, 501.35, 0.9542394014962593), (80, 468.275, 0.9534912718204489), (90, 438.975, 0.9485349127182044), (100, 419.4, 0.9442643391521197), (110, 390.625, 0.941147132169576), (120, 374.9, 0.9634663341645885), (130, 348.225, 0.9353491271820449), (140, 333.35, 0.9533042394014962), (150, 311.05, 0.9271508728179552), (160, 296.875, 0.9211970074812967), (170, 265.3, 0.8898067331670823), (180, 245.3, 0.8482543640897756), (190, 226.075, 0.8389027431421446), (200, 215.525, 0.8290523690773067), (210, 172.675, 0.6923316708229427), (220, 174.775, 0.7435473815461346), (230, 171.4, 0.7783354114713217), (240, 141.6, 0.7126870324189526), (250, 122.7, 0.6941708229426434), (260, 88.6, 0.5562032418952618), (270, 91.95, 0.5902743142144639), (280, 70.65, 0.4587281795511222), (290, 64.0, 0.46580423940149623), (300, 44.975, 0.3331359102244389), (310, 45.5, 0.3332605985037406), (320, 47.1, 0.3773690773067332), (330, 32.1, 0.2682356608478803), (340, 36.85, 0.31798628428927683)]
rmin = [x[0] for x in raw]
frw_n = [100*x[1]/802 for x in raw]
recv_n = [100*x[2] for x in raw]
 

plt.plot(rmin, frw_n, 'r--', label='forwarders')
plt.plot(rmin, recv_n, 'b--', label='receivers')
plt.ylim(0,100)
plt.legend(loc='upper right')
plt.xlabel('Rmin, m')
plt.ylabel('% total nodes')
title = "LUXEMBURG 50: %receivers (blue) forwaredrs (red) vs rmin WITH OUTLIERS"
#plt.title(title)
plt.savefig(title+'.png')
#plt.show()
plt.clf()







# LUXEMBURG 100 NO OUTLIERS
raw = [(50, 712.175, 0.9818116274496952), (60, 733.6, 0.9817870485678705), (70, 672.925, 0.9817032282785707), (80, 659.65, 0.9817559153175591), (90, 604.525, 0.9817032282785707), (100, 587.05, 0.9815068493150685), (110, 552.975, 0.9816313823163139), (120, 519.85, 0.9817559153175591), (130, 490.6, 0.9817247820672478), (140, 454.6, 0.9582503113325032), (150, 436.6, 0.9806814190375834), (160, 403.425, 0.9797234728741578), (170, 389.275, 0.9772104607721046), (180, 349.825, 0.9474782067247821), (190, 325.9, 0.941002490660025), (200, 257.95, 0.9351360967799324), (210, 263.5, 0.9217038669093464), (220, 233.25, 0.90745231696926), (230, 215.725, 0.8535491905354919), (240, 188.475, 0.8740348692403487), (250, 170.975, 0.8403175591531756), (260, 154.725, 0.837266500622665), (270, 141.575, 0.8450219571344301), (280, 131.225, 0.7990228949133059), (290, 122.2, 0.8037487626528722), (300, 114.35, 0.8031739949548169), (310, 93.75, 0.7340686710549724), (320, 98.1, 0.7738211436841573), (330, 103.375, 0.791582846377367), (340, 80.95, 0.7482602007178961)]
rmin = [x[0] for x in raw]
frw_n = [100*x[1]/802 for x in raw]
recv_n = [100*x[2] for x in raw]
 

plt.plot(rmin, frw_n, 'r--', label='forwarders')
plt.plot(rmin, recv_n, 'b--', label='receivers')
plt.ylim(0,100)
plt.legend(loc='upper right')
plt.xlabel('Rmin, m')
plt.ylabel('% total nodes')
title = "LUXEMBURG 100: %receivers (blue) forwaredrs (red) vs rmin NO OUTLIERS"
#plt.title(title)
plt.savefig(title+'.png')
#plt.show()
plt.clf()


# LUXEMBURG 100 WITH OUTLIERS
raw = [(50, 750.65, 0.9817870485678705), (60, 713.625, 0.9572851805728518), (70, 671.925, 0.9572229140722291), (80, 643.625, 0.9574097135740971), (90, 620.1, 0.9817247820672478), (100, 557.9, 0.9326587795765878), (110, 554.65, 0.9817870485678705), (120, 482.075, 0.9084059775840597), (130, 479.25, 0.9573785803237858), (140, 467.625, 0.9810709838107098), (150, 434.225, 0.9565068493150685), (160, 384.65, 0.9095890410958904), (170, 352.425, 0.8822229140722292), (180, 328.575, 0.9002179327521793), (190, 333.5, 0.9619551681195517), (200, 283.075, 0.9128891656288917), (210, 260.2, 0.889508094645081), (220, 237.7, 0.8826276463262764), (230, 203.9, 0.8350560398505604), (240, 184.9, 0.8395703611457036), (250, 170.2, 0.8652241594022416), (260, 156.75, 0.8339975093399751), (270, 118.825, 0.6769925280199253), (280, 136.975, 0.8029576587795766), (290, 115.1, 0.7283001245330012), (300, 112.75, 0.7457658779576588), (310, 114.75, 0.7825342465753424), (320, 93.1, 0.686425902864259), (330, 90.825, 0.6951120797011208), (340, 87.675, 0.6822540473225405)]
rmin = [x[0] for x in raw]
frw_n = [100*x[1]/802 for x in raw]
recv_n = [100*x[2] for x in raw]
 

plt.plot(rmin, frw_n, 'r--', label='forwarders')
plt.plot(rmin, recv_n, 'b--', label='receivers')
plt.ylim(0,100)
plt.legend(loc='upper right')
plt.xlabel('Rmin, m')
plt.ylabel('% total nodes')
title = "LUXEMBURG 100: %receivers (blue) forwaredrs (red) vs rmin WITH OUTLIERS"
#plt.title(title)
plt.savefig(title+'.png')
#plt.show()
plt.clf()









# LUXEMBURG 150 NO OUTLIERS
raw = [(50, 759.8, 0.9817870485678705), (60, 731.275, 0.9817990228949133), (70, 731.75, 0.9817870485678705), (80, 717.3, 0.9817870485678705), (90, 699.425, 0.9817870485678705), (100, 660.075, 0.9817351598173516), (110, 627.275, 0.9816712967397899), (120, 597.775, 0.9816625155666252), (130, 568.1, 0.9817559153175591), (140, 533.375, 0.9817032282785707), (150, 519.35, 0.9815691158156912), (160, 482.625, 0.9815068493150685), (170, 421.525, 0.9791571082126237), (180, 395.925, 0.9766899766899767), (190, 335.575, 0.971426594714266), (200, 329.525, 0.9603410288341795), (210, 316.4, 0.9653798256537982), (220, 285.575, 0.9562218603314494), (230, 260.925, 0.9538605230386052), (240, 220.95, 0.9416291471085991), (250, 197.85, 0.8935554171855542), (260, 180.925, 0.9397771178593096), (270, 173.475, 0.9079078455790784), (280, 163.0, 0.8998307628444615), (290, 155.975, 0.8786737235367372), (300, 141.125, 0.8886227927323818), (310, 139.4, 0.882460005747677), (320, 125.925, 0.887213489953216), (330, 128.125, 0.8778331257783313), (340, 114.375, 0.8814642459199056)]
rmin = [x[0] for x in raw]
frw_n = [100*x[1]/802 for x in raw]
recv_n = [100*x[2] for x in raw]
 

plt.plot(rmin, frw_n, 'r--', label='forwarders')
plt.plot(rmin, recv_n, 'b--', label='receivers')
plt.ylim(0,100)
plt.legend(loc='upper right')
plt.xlabel('Rmin, m')
plt.ylabel('% total nodes')
title = "LUXEMBURG 150: %receivers (blue) forwaredrs (red) vs rmin NO OUTLIERS"
#plt.title(title)
plt.savefig(title+'.png')
#plt.show()
plt.clf()




# LUXEMBURG 150 WITH OUTLIERS
raw = [(50, 759.55, 0.9817870485678705), (60, 711.625, 0.9330635118306351), (70, 676.525, 0.9089352428393525), (80, 717.75, 0.9817870485678705), (90, 698.375, 0.9817870485678705), (100, 644.05, 0.9331569115815691), (110, 625.8, 0.9571917808219178), (120, 571.775, 0.9328455790784558), (130, 572.85, 0.9817559153175591), (140, 545.45, 0.9816625155666252), (150, 520.2, 0.9814134495641345), (160, 485.2, 0.9811955168119552), (170, 443.325, 0.9795143212951433), (180, 383.0, 0.928082191780822), (190, 351.3, 0.9219489414694895), (200, 320.85, 0.9066625155666251), (210, 316.825, 0.9584682440846825), (220, 281.3, 0.9526151930261519), (230, 247.225, 0.8831569115815692), (240, 209.2, 0.8785491905354919), (250, 203.725, 0.9174968866749689), (260, 172.9, 0.8602428393524284), (270, 174.425, 0.90093399750934), (280, 168.3, 0.9026774595267746), (290, 154.05, 0.8791407222914073), (300, 143.075, 0.862453300124533), (310, 132.75, 0.8202988792029888), (320, 126.975, 0.8492839352428394), (330, 123.375, 0.8421544209215442), (340, 120.35, 0.8801369863013698)]
rmin = [x[0] for x in raw]
frw_n = [100*x[1]/802 for x in raw]
recv_n = [100*x[2] for x in raw]
 

plt.plot(rmin, frw_n, 'r--', label='forwarders')
plt.plot(rmin, recv_n, 'b--', label='receivers')
plt.ylim(0,100)
plt.legend(loc='upper right')
plt.xlabel('Rmin, m')
plt.ylabel('% total nodes')
title = "LUXEMBURG 150: %receivers (blue) forwaredrs (red) vs rmin WITH OUTLIERS"
#plt.title(title)
plt.savefig(title+'.png')
#plt.show()
plt.clf()









# - - - - - - - - - - - -  COLOGNEEEEE - - - - - - - - - -




# COLOGNE 50 NO OUTLIERS
raw = [(50, 120.725, 0.316769801980198), (60, 119.925, 0.2880905233380481), (70, 121.75, 0.3046592894583576), (80, 121.975, 0.34480996486745447), (90, 116.55, 0.3215121512151215), (100, 102.85, 0.3207920792079208), (110, 84.95, 0.3112446958981612), (120, 93.475, 0.3131806930693069), (130, 102.2, 0.36070544554455447), (140, 72.45, 0.3117711771177118), (150, 75.125, 0.33762376237623765), (160, 65.75, 0.27400990099009903), (170, 64.475, 0.27662766276627665), (180, 55.525, 0.28578728840626), (190, 47.325, 0.2907957462412908), (200, 49.325, 0.26489939316512295), (210, 42.475, 0.32252475247524753), (220, 46.75, 0.299009900990099), (230, 28.0, 0.2507963839862247), (240, 31.7, 0.2536237623762376), (250, 28.0, 0.2507650765076508), (260, 33.525, 0.25597359735973596), (270, 21.825, 0.21283168316831683), (280, 25.2, 0.22515584891822515), (290, 13.95, 0.16727958510136728), (300, 21.425, 0.2129108910891089), (310, 17.75, 0.21856435643564356), (320, 18.725, 0.18792079207920792), (330, 15.2, 0.2243650452001722), (340, 9.85, 0.16602397081813444)]
rmin = [x[0] for x in raw]
frw_n = [100*x[1]/503 for x in raw]
recv_n = [100*x[2] for x in raw]
 

plt.plot(rmin, frw_n, 'r--', label='forwarders')
plt.plot(rmin, recv_n, 'b--', label='receivers')
plt.ylim(0,100)
plt.legend(loc='upper right')
plt.xlabel('Rmin, m')
plt.ylabel('% total nodes')
title = "COLOGNE 50: %receivers (blue) forwaredrs (red) vs rmin NO OUTLIERS"
#plt.title(title)
plt.savefig(title+'.png')
#plt.show()
plt.clf()



# COLOGNE 50 WITH OUTLIERS
raw = [(50, 117.9, 0.24757425742574257), (60, 138.975, 0.29495049504950493), (70, 116.8, 0.25485148514851486), (80, 121.3, 0.2657920792079208), (90, 100.075, 0.22975247524752476), (100, 94.875, 0.22693069306930694), (110, 83.325, 0.21762376237623762), (120, 93.95, 0.2545049504950495), (130, 90.725, 0.25103960396039604), (140, 91.35, 0.26801980198019804), (150, 73.025, 0.23455445544554454), (160, 65.7, 0.22054455445544555), (170, 52.575, 0.20103960396039605), (180, 48.875, 0.19178217821782179), (190, 41.175, 0.1893069306930693), (200, 52.9, 0.23534653465346533), (210, 38.3, 0.16), (220, 45.25, 0.20212871287128714), (230, 37.3, 0.1945049504950495), (240, 37.675, 0.19564356435643565), (250, 41.65, 0.21663366336633663), (260, 30.225, 0.1741089108910891), (270, 28.1, 0.18262376237623762), (280, 25.175, 0.15866336633663367), (290, 20.075, 0.1313861386138614), (300, 15.175, 0.1100990099009901), (310, 16.925, 0.13237623762376238), (320, 18.725, 0.14747524752475247), (330, 16.75, 0.13341584158415842), (340, 17.75, 0.15212871287128713)]
rmin = [x[0] for x in raw]
frw_n = [100*x[1]/503 for x in raw]
recv_n = [100*x[2] for x in raw]
 

plt.plot(rmin, frw_n, 'r--', label='forwarders')
plt.plot(rmin, recv_n, 'b--', label='receivers')
plt.ylim(0,100)
plt.legend(loc='upper right')
plt.xlabel('Rmin, m')
plt.ylabel('% total nodes')
title = "COLOGNE 50: %receivers (blue) forwaredrs (red) vs rmin WITH OUTLIERS"
#plt.title(title)
plt.savefig(title+'.png')
#plt.show()
plt.clf()







# COLOGNE 100 NO OUTLIERS
raw = [(50, 411.375, 0.8675839698650204), (60, 389.7, 0.8676275679257787), (70, 368.05, 0.8676762951701555), (80, 400.375, 0.8676051797324164), (90, 378.775, 0.867651235444476), (100, 389.575, 0.8676275679257787), (110, 389.525, 0.8676275679257787), (120, 389.525, 0.8676275679257787), (130, 323.825, 0.8677932405566601), (140, 356.05, 0.8674618952948973), (150, 356.275, 0.8677028736670884), (160, 388.6, 0.8676275679257787), (170, 377.4, 0.867651235444476), (180, 377.15, 0.867651235444476), (190, 344.675, 0.8674826043737575), (200, 376.4, 0.867651235444476), (210, 396.025, 0.8676051797324164), (220, 374.675, 0.867651235444476), (230, 374.6, 0.8675376313547287), (240, 416.375, 0.8653208951419687), (250, 383.45, 0.8634857521537442), (260, 394.1, 0.8636290365912632), (270, 383.45, 0.8636514247846255), (280, 394.1, 0.8636290365912632), (290, 361.675, 0.8623552800842007), (300, 382.925, 0.8624917163684559), (310, 382.8, 0.8618290258449304), (320, 340.35, 0.862263916500994), (330, 371.45, 0.8589037205339393), (340, 318.425, 0.8591119946984758)]
rmin = [x[0] for x in raw]
frw_n = [100*x[1]/503 for x in raw]
recv_n = [100*x[2] for x in raw]
 

plt.plot(rmin, frw_n, 'r--', label='forwarders')
plt.plot(rmin, recv_n, 'b--', label='receivers')
plt.ylim(0,100)
plt.legend(loc='upper right')
plt.xlabel('Rmin, m')
plt.ylabel('% total nodes')
title = "COLOGNE 100: %receivers (blue) forwaredrs (red) vs rmin NO OUTLIERS"
#plt.title(title)
plt.savefig(title+'.png')
#plt.show()
plt.clf()


# COLOGNE 100 WITH OUTLIERS
raw = [(50, 337.925, 0.6772365805168986), (60, 381.2, 0.763817097415507), (70, 359.2, 0.7198807157057654), (80, 391.65, 0.7848409542743539), (90, 370.075, 0.741948310139165), (100, 349.85, 0.7011431411530815), (110, 338.1, 0.677882703777336), (120, 381.3, 0.76441351888668), (130, 379.2, 0.762127236580517), (140, 379.525, 0.7627733598409543), (150, 369.55, 0.7424950298210735), (160, 358.65, 0.7207256461232604), (170, 389.775, 0.7838469184890656), (180, 368.1, 0.7414015904572565), (190, 356.825, 0.7183399602385686), (200, 325.8, 0.6574055666003976), (210, 386.375, 0.7832007952286282), (220, 376.85, 0.763817097415507), (230, 357.05, 0.723558648111332), (240, 375.225, 0.7603876739562624), (250, 395.3, 0.8009443339960238), (260, 364.05, 0.7378230616302187), (270, 395.15, 0.8009443339960238), (280, 372.975, 0.7565109343936381), (290, 353.625, 0.7170477137176938), (300, 372.975, 0.7560636182902585), (310, 383.575, 0.777286282306163), (320, 321.6, 0.6518886679920477), (330, 373.625, 0.7560636182902585), (340, 393.775, 0.7969184890656064)]
rmin = [x[0] for x in raw]
frw_n = [100*x[1]/503 for x in raw]
recv_n = [100*x[2] for x in raw]
 

plt.plot(rmin, frw_n, 'r--', label='forwarders')
plt.plot(rmin, recv_n, 'b--', label='receivers')
plt.ylim(0,100)
plt.legend(loc='upper right')
plt.xlabel('Rmin, m')
plt.ylabel('% total nodes')
title = "COLOGNE 100: %receivers (blue) forwaredrs (red) vs rmin WITH OUTLIERS"
#plt.title(title)
plt.savefig(title+'.png')
#plt.show()
plt.clf()







# COLOGNE 150 NO OUTLIERS
raw = [(50, 190.4, 0.44653465346534654), (60, 176.45, 0.44449621432731506), (70, 188.8, 0.44426010168584423), (80, 181.125, 0.434037998394434), (90, 157.05, 0.44474009900990097), (100, 146.125, 0.43254950495049505), (110, 153.575, 0.42684268426842686), (120, 139.45, 0.43192319231923193), (130, 145.975, 0.4470721357850071), (140, 122.65, 0.4344059405940594), (150, 124.35, 0.4589400116482236), (160, 123.675, 0.4327000267594327), (170, 105.65, 0.429120559114735), (180, 96.775, 0.41806930693069305), (190, 93.525, 0.41974197419741976), (200, 84.925, 0.4059988351776354), (210, 81.675, 0.4211997670355271), (220, 72.8, 0.39304101838755306), (230, 73.8, 0.368264721208963), (240, 52.8, 0.32127212721272125), (250, 53.75, 0.3379349363507779), (260, 50.725, 0.3102310231023102), (270, 49.175, 0.29965212737489966), (280, 34.8, 0.2847949080622348), (290, 36.65, 0.2807080708070807), (300, 28.95, 0.23774752475247524), (310, 31.7, 0.27360874018436326), (320, 34.525, 0.2762958648806057), (330, 24.75, 0.2293197061641648), (340, 31.275, 0.2646864686468647)]
rmin = [x[0] for x in raw]
frw_n = [100*x[1]/503 for x in raw]
recv_n = [100*x[2] for x in raw]
 

plt.plot(rmin, frw_n, 'r--', label='forwarders')
plt.plot(rmin, recv_n, 'b--', label='receivers')
plt.ylim(0,100)
plt.legend(loc='upper right')
plt.xlabel('Rmin, m')
plt.ylabel('% total nodes')
title = "COLOGNE 150: %receivers (blue) forwaredrs (red) vs rmin NO OUTLIERS"
#plt.title(title)
plt.savefig(title+'.png')
#plt.show()
plt.clf()




# COLOGNE 150 WITH OUTLIERS
raw = [(50, 167.475, 0.35316831683168315), (60, 195.25, 0.4179207920792079), (70, 175.925, 0.38415841584158417), (80, 170.075, 0.376980198019802), (90, 184.875, 0.42034653465346533), (100, 168.55, 0.39871287128712873), (110, 164.95, 0.4115346534653465), (120, 141.9, 0.36247524752475246), (130, 140.475, 0.3774752475247525), (140, 138.0, 0.39004950495049506), (150, 129.0, 0.3866831683168317), (160, 106.35, 0.34747524752475245), (170, 114.25, 0.3785148514851485), (180, 100.6, 0.3503465346534653), (190, 96.65, 0.36336633663366336), (200, 78.4, 0.333960396039604), (210, 78.3, 0.32564356435643566), (220, 70.7, 0.3205940594059406), (230, 64.075, 0.31084158415841584), (240, 56.925, 0.28668316831683166), (250, 58.525, 0.28975247524752473), (260, 42.225, 0.25663366336633664), (270, 34.65, 0.21217821782178217), (280, 46.175, 0.26752475247524754), (290, 31.65, 0.19212871287128713), (300, 39.575, 0.2592079207920792), (310, 36.175, 0.2256930693069307), (320, 32.725, 0.23430693069306932), (330, 33.9, 0.23886138613861385), (340, 24.3, 0.19084158415841584)]
rmin = [x[0] for x in raw]
frw_n = [100*x[1]/503 for x in raw]
recv_n = [100*x[2] for x in raw]
 

plt.plot(rmin, frw_n, 'r--', label='forwarders')
plt.plot(rmin, recv_n, 'b--', label='receivers')
plt.ylim(0,100)
plt.legend(loc='upper right')
plt.xlabel('Rmin, m')
plt.ylabel('% total nodes')
title = "COLOGNE 150: %receivers (blue) forwaredrs (red) vs rmin WITH OUTLIERS"
#plt.title(title)
plt.savefig(title+'.png')
#plt.show()
plt.clf()






# COLOGNE 500 NO OUTLIERS
raw = [(50, 382.975, 0.8661493176344661), (60, 358.15, 0.8661951909476662), (70, 340.35, 0.8649970879440885), (80, 344.875, 0.8651202263083452), (90, 326.925, 0.8648806057076296), (100, 337.0, 0.8636413641364137), (110, 274.55, 0.8633663366336634), (120, 283.725, 0.8601860186018602), (130, 262.525, 0.8564356435643564), (140, 257.1, 0.8524452445244525), (150, 258.75, 0.8504667609618105), (160, 233.65, 0.845602795573675), (170, 216.275, 0.8357018054746651), (180, 207.55, 0.8264997087944088), (190, 206.625, 0.8272135785007072), (200, 181.65, 0.8238223822382238), (210, 169.975, 0.821002100210021), (220, 173.1, 0.7854963874765855), (230, 141.55, 0.7708370837083708), (240, 126.325, 0.6880605707629587), (250, 103.05, 0.6113861386138614), (260, 96.325, 0.6352103960396039), (270, 78.45, 0.4385335830880385), (280, 83.9, 0.5185918591859185), (290, 64.525, 0.44305516265912304), (300, 64.2, 0.48155940594059404), (310, 64.65, 0.4355365266256355), (320, 57.975, 0.4106710671067107), (330, 57.4, 0.42885431400282886), (340, 55.175, 0.4423762376237624)]
rmin = [x[0] for x in raw]
frw_n = [100*x[1]/503 for x in raw]
recv_n = [100*x[2] for x in raw]
 

plt.plot(rmin, frw_n, 'r--', label='forwarders')
plt.plot(rmin, recv_n, 'b--', label='receivers')
plt.ylim(0,100)
plt.legend(loc='upper right')
plt.xlabel('Rmin, m')
plt.ylabel('% total nodes')
title = "COLOGNE 500: %receivers (blue) forwaredrs (red) vs rmin NO OUTLIERS"
#plt.title(title)
plt.savefig(title+'.png')
#plt.show()
plt.clf()




# COLOGNE 500 WITH OUTLIERS
raw = [(50, 373.85, 0.7823762376237624), (60, 329.025, 0.6965346534653465), (70, 341.975, 0.7385148514851485), (80, 337.275, 0.7394059405940594), (90, 366.7, 0.8236633663366336), (100, 302.7, 0.6986138613861386), (110, 310.0, 0.7572277227722772), (120, 318.725, 0.7963861386138614), (130, 289.6, 0.7562871287128713), (140, 272.175, 0.7494554455445545), (150, 250.4, 0.7218811881188119), (160, 249.525, 0.764950495049505), (170, 234.275, 0.7679207920792079), (180, 208.9, 0.7103960396039604), (190, 198.575, 0.7082673267326732), (200, 182.025, 0.6866336633663367), (210, 167.425, 0.6658910891089109), (220, 176.95, 0.7470792079207921), (230, 142.8, 0.6464851485148515), (240, 94.4, 0.4500990099009901), (250, 113.975, 0.5528217821782179), (260, 87.375, 0.47059405940594057), (270, 81.2, 0.4271287128712871), (280, 71.7, 0.39584158415841586), (290, 69.0, 0.4166336633663366), (300, 60.4, 0.351039603960396), (310, 51.075, 0.32232673267326734), (320, 54.45, 0.3505445544554455), (330, 43.65, 0.3006930693069307), (340, 54.7, 0.37113861386138614)]
rmin = [x[0] for x in raw]
frw_n = [100*x[1]/503 for x in raw]
recv_n = [100*x[2] for x in raw]
 

plt.plot(rmin, frw_n, 'r--', label='forwarders')
plt.plot(rmin, recv_n, 'b--', label='receivers')
plt.ylim(0,100)
plt.legend(loc='upper right')
plt.xlabel('Rmin, m')
plt.ylabel('% total nodes')
title = "COLOGNE 500: %receivers (blue) forwaredrs (red) vs rmin WITH OUTLIERS"
#plt.title(title)
plt.savefig(title+'.png')
#plt.show()
plt.clf()





# COLOGNE 1000 NO OUTLIERS
raw = [(50, 331.32, 86.60891089108911), (60, 352.24, 86.60373014045591), (70, 360.74, 86.45984598459846), (80, 324.02, 86.4670369475972), (90, 331.16, 86.45636656688924), (100, 329.88, 86.36363636363636), (110, 311.08, 86.33663366336634), (120, 316.74, 86.02238484718038), (130, 275.8, 85.75200377180575), (140, 304.74, 85.24146292180238), (150, 277.82, 84.95049504950495), (160, 215.38, 84.65600406194466), (170, 205.2, 83.66336633663366), (180, 207.2, 83.32390381895333), (190, 201.66, 82.74925166935299), (200, 190.5, 80.85958595859586), (210, 190.34, 82.2083512699096), (220, 145.1, 82.17286593524217), (230, 142.24, 74.02717015887636), (240, 113.28, 64.83941077034532), (250, 103.58, 57.398739873987395), (260, 98.52, 58.55085508550855), (270, 78.08, 46.35044899838821), (280, 56.74, 42.477923468022475), (290, 65.6, 46.71335426225549), (300, 67.38, 45.98204006447156), (310, 67.44, 46.64266426642664), (320, 46.4, 40.72433559145388), (330, 40.66, 37.964796479647966), (340, 48.58, 44.67952058363731)] 
rmin = [x[0] for x in raw]
frw_n = [100*x[1]/501 for x in raw]
recv_n = [x[2] for x in raw]
 

plt.plot(rmin, frw_n, 'r--', label='forwarders')
plt.plot(rmin, recv_n, 'b--', label='receivers')
plt.ylim(0,100)
plt.legend(loc='upper right')
plt.xlabel('Rmin, m')
plt.ylabel('% total nodes')
title = "COLOGNE 1000: %receivers (blue) forwaredrs (red) vs rmin NO OUTLIERS"
#plt.title(title)
plt.savefig(title+'.png')
#plt.show()
plt.clf()




# COLOGNE 1000 WITH OUTLIERS
raw = [(50, 389.34, 81.43366336633663), (60, 377.94, 79.9009900990099), (70, 323.02, 69.82178217821782), (80, 341.68, 74.74059405940594), (90, 348.28, 78.17029702970297), (100, 331.16, 76.30495049504951), (110, 326.46, 79.64752475247525), (120, 270.18, 67.81782178217821), (130, 270.24, 70.8079207920792), (140, 264.28, 72.16633663366336), (150, 244.5, 70.1108910891089), (160, 243.5, 74.75643564356436), (170, 191.4, 62.64554455445545), (180, 214.48, 72.13465346534653), (190, 210.62, 74.7128712871287), (200, 199.56, 74.63762376237624), (210, 164.96, 65.16039603960397), (220, 150.76, 63.68316831683168), (230, 149.94, 67.12475247524752), (240, 119.34, 56.035643564356434), (250, 107.54, 53.42970297029703), (260, 85.9, 45.27524752475247), (270, 77.0, 39.27524752475247), (280, 70.34, 38.01980198019802), (290, 57.0, 33.90891089108911), (300, 65.84, 39.504950495049506), (310, 48.74, 30.095049504950495), (320, 50.68, 33.42970297029703), (330, 51.92, 34.744554455445545), (340, 34.96, 24.03960396039604)]
rmin = [x[0] for x in raw]
frw_n = [100*x[1]/501 for x in raw]
recv_n = [x[2] for x in raw]
 

plt.plot(rmin, frw_n, 'r--', label='forwarders')
plt.plot(rmin, recv_n, 'b--', label='receivers')
plt.ylim(0,100)
plt.legend(loc='upper right')
plt.xlabel('Rmin, m')
plt.ylabel('% total nodes')
title = "COLOGNE 1000: %receivers (blue) forwaredrs (red) vs rmin WITH OUTLIERS"
#plt.title(title)
plt.savefig(title+'.png')
#plt.show()
plt.clf()



