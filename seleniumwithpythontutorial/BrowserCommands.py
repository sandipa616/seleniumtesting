from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/?flo=true")
driver.maximize_window()  # safer than fullscreen
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,".x1i10hfl.xjqpnuy.xc5r6h4.xqeqjp1.x1phubyo.xdl72j9.x2lah0s.x3ct3a4.xdj266r.x14z9mp.xat24cr.x1lziwak.x2lwn1j.xeuugli.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x1a2a7pz.x6s0dn4.xjyslct.x1ejq31n.x18oe1m7.x1sy0etr.xstzfhl.x9f619.x1ypdohk.x1f6kntn.xl56j7k.x17ydfre.x2b8uid.xlyipyv.x87ps6o.x14atkfc.x5c86q.x18br7mf.x1i0vuye.x11q7cde.xr5sc7.xf8g3cd.x20cjte.xt0b8zv.x568u83.xjbqb8w.xr9e8f9.x1e4oeot.x1ui04y5.x6en5u8.x972fbf.x10w94by.x1qhh985.x14e42zd.xt7dq6l.xexx8yu.xyri2b.x18d9i69.x1c1uobl.x1n2onr6.x1n5bzlp.x3nfvp2").click()
time.sleep(5)
driver.back();
time.sleep(5)
driver.forward();
time.sleep(5)
driver.refresh();
driver.close();
