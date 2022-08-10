
from bs4 import BeautifulSoup
import re
import requests
import pandas as pd


# req = requests.get("http://serateshgh.com")
# source = req.text   
# # Because the request is not answered, we entered the source code manually
source = """
    					
							<div class="entry">
								<p>سید احسان خاندوزی وزیر اقتصاد</p>
								<a class="more-link" href="http://serateshgh.com/212068/%d8%a7%d9%86%d8%aa%d8%b4%d8%a7%d8%b1-%d8%af%d8%a7%d8%af%d9%87%e2%80%8c%d9%87%d8%a7%db%8c-%d8%ba%d9%84%d8%b7-%d8%a7%d9%82%d8%aa%d8%b5%d8%a7%d8%af%db%8c-%d9%81%d8%a7%db%8c%d8%af%d9%87%e2%80%8c%d8%a7/">ادامه نوشته &raquo;</a>
							</div>
						</div>
					</li><!-- .first-news -->
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211978/%d8%a7%d9%88%d8%b1%d8%a7%d8%b3%db%8c%d8%a7-%d8%b1%db%8c%d9%88%db%8c%d9%88-%d9%87%d9%85%d9%87-%d9%85%d8%ad%d9%88%d8%b1-%d9%85%d9%82%d8%a7%d9%88%d9%85%d8%aa-%d8%a8%d9%87-%d9%85%d9%88%d8%b4%da%a9/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/636317427760903338-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211978/%d8%a7%d9%88%d8%b1%d8%a7%d8%b3%db%8c%d8%a7-%d8%b1%db%8c%d9%88%db%8c%d9%88-%d9%87%d9%85%d9%87-%d9%85%d8%ad%d9%88%d8%b1-%d9%85%d9%82%d8%a7%d9%88%d9%85%d8%aa-%d8%a8%d9%87-%d9%85%d9%88%d8%b4%da%a9/" rel="bookmark">اوراسیا ریویو: همه محور مقاومت به موشک‌های ایران مسلح شده‌اند</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/gilan_53/" title="">گیلان </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>11 ساعت قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/212063/%d8%ae%d8%b7%d8%a8%d9%87-%db%8c-%d8%a7%d9%85%d8%a7%d9%85-%d8%ad%d8%b3%db%8c%d9%86-%d8%b9%d9%84%db%8c%d9%87-%d8%a7%d9%84%d8%b3%d9%84%d8%a7%d9%85-%d8%af%d8%b1-%d8%b3%d8%b1%d8%b2%d9%85%db%8c%d9%86-%d9%85/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/1-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/212063/%d8%ae%d8%b7%d8%a8%d9%87-%db%8c-%d8%a7%d9%85%d8%a7%d9%85-%d8%ad%d8%b3%db%8c%d9%86-%d8%b9%d9%84%db%8c%d9%87-%d8%a7%d9%84%d8%b3%d9%84%d8%a7%d9%85-%d8%af%d8%b1-%d8%b3%d8%b1%d8%b2%d9%85%db%8c%d9%86-%d9%85/" rel="bookmark">خطبه ی امام حسین علیه السلام در سرزمین منا سال ۵۸ هجری</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/nasr_29/" title="">نصر </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>11 ساعت قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/212071/%d8%af%d9%85%d8%b4%d9%82-%d8%a2%d9%85%d8%b1%db%8c%da%a9%d8%a7-%d8%b1%d9%88%d8%b2%d8%a7%d9%86%d9%87-66-%d9%87%d8%b2%d8%a7%d8%b1-%d8%a8%d8%b4%da%a9%d9%87-%d9%86%d9%81%d8%aa-%d8%b3%d9%88%d8%b1%db%8c/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/14010519000343_Test_PhotoN-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/212071/%d8%af%d9%85%d8%b4%d9%82-%d8%a2%d9%85%d8%b1%db%8c%da%a9%d8%a7-%d8%b1%d9%88%d8%b2%d8%a7%d9%86%d9%87-66-%d9%87%d8%b2%d8%a7%d8%b1-%d8%a8%d8%b4%da%a9%d9%87-%d9%86%d9%81%d8%aa-%d8%b3%d9%88%d8%b1%db%8c/" rel="bookmark">دمشق: آمریکا روزانه 66 هزار بشکه نفت سوریه را سرقت می‌کند</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/hamsayeh_36/" title="">همسایه </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>11 ساعت قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/212057/%d8%b5%d9%81%e2%80%8c%d8%a2%d8%b1%d8%a7%db%8c%db%8c-%da%a9%d8%b4%d8%aa%db%8c%e2%80%8c%d9%87%d8%a7%db%8c-%d8%ac%d9%86%da%af%db%8c-%d8%aa%d8%a7%db%8c%d9%88%d8%a7%d9%86%db%8c-%d9%88-%da%86%db%8c%d9%86/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/14010519000235_Test_PhotoN-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/212057/%d8%b5%d9%81%e2%80%8c%d8%a2%d8%b1%d8%a7%db%8c%db%8c-%da%a9%d8%b4%d8%aa%db%8c%e2%80%8c%d9%87%d8%a7%db%8c-%d8%ac%d9%86%da%af%db%8c-%d8%aa%d8%a7%db%8c%d9%88%d8%a7%d9%86%db%8c-%d9%88-%da%86%db%8c%d9%86/" rel="bookmark">صف‌آرایی کشتی‌های جنگی تایوانی و چینی مقابل یکدیگر</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/msafr/" title="">مسافر </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>13 ساعت قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news tie_video">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211952/%d8%b1%d8%a7%d9%87%da%a9%d8%a7%d8%b1-%d8%b3%d8%b1%db%8c%d8%b9-%d8%a7%d9%81%d8%b2%d8%a7%db%8c%d8%b4-%d9%81%d8%a7%d9%84%d9%88%d8%b1/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/sci9z_راهکار-سریع-افزایش-فالور-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211952/%d8%b1%d8%a7%d9%87%da%a9%d8%a7%d8%b1-%d8%b3%d8%b1%db%8c%d8%b9-%d8%a7%d9%81%d8%b2%d8%a7%db%8c%d8%b4-%d9%81%d8%a7%d9%84%d9%88%d8%b1/" rel="bookmark">راهکار سریع افزایش فالور</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/abas_ghre_daghi/" title="">عباس قره داغی </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>15 ساعت قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/clip/" rel="category tag">کلیپ‌های دیگران</a></span>
	
</p>
					
					</li>
																		<li class="other-news tie_video">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211949/%d8%b2%d9%86%d8%af%d9%87-%d9%86%da%af%d9%87%d8%af%d8%a7%d8%b4%d8%aa%d9%86-%d8%b9%d8%a7%d8%b4%d9%88%d8%b1%d8%a7-%d9%85%d8%b3%d8%a6%d9%84%d9%87-%d8%a8%d8%b3%db%8c%d8%a7%d8%b1-%d9%85%d9%87%d9%85-%d8%b3/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/IMG-20151020-WA0014-e1660091807594-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211949/%d8%b2%d9%86%d8%af%d9%87-%d9%86%da%af%d9%87%d8%af%d8%a7%d8%b4%d8%aa%d9%86-%d8%b9%d8%a7%d8%b4%d9%88%d8%b1%d8%a7-%d9%85%d8%b3%d8%a6%d9%84%d9%87-%d8%a8%d8%b3%db%8c%d8%a7%d8%b1-%d9%85%d9%87%d9%85-%d8%b3/" rel="bookmark">زنده نگهداشتن عاشورا مسئله بسیار مهم سیاسی و عبادی است</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/abas_ghre_daghi/" title="">عباس قره داغی </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>16 ساعت قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/clip/" rel="category tag">کلیپ‌های دیگران</a></span>
	
</p>
					
					</li>
																		<li class="other-news tie_video">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211943/%d8%aa%d8%af%d8%a7%d8%a8%db%8c%d8%b1-%d8%ba%d8%b0%d8%a7%db%8c%db%8c-%d8%b3%d8%a7%d8%af%d9%87-%d8%a8%d8%b1%d8%a7%db%8c-%d8%b1%d9%81%d8%b9-%d9%81%d9%88%d8%b1%db%8c-%d8%b3%d8%b1%d8%af%db%8c-%d8%aa%d9%86/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/1399091009081958721717714-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211943/%d8%aa%d8%af%d8%a7%d8%a8%db%8c%d8%b1-%d8%ba%d8%b0%d8%a7%db%8c%db%8c-%d8%b3%d8%a7%d8%af%d9%87-%d8%a8%d8%b1%d8%a7%db%8c-%d8%b1%d9%81%d8%b9-%d9%81%d9%88%d8%b1%db%8c-%d8%b3%d8%b1%d8%af%db%8c-%d8%aa%d9%86/" rel="bookmark">تدابیر غذایی ساده برای رفع فوری سردی تن  و معده</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/abas_ghre_daghi/" title="">عباس قره داغی </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>17 ساعت قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/%d8%af%d8%b1%d9%85%d8%a7%d9%86%e2%80%8c%d9%87%d8%a7%db%8c-%d8%b3%d8%a7%d8%af%d9%87/" rel="category tag">درمان‌های ساده</a>, <a href="http://serateshgh.com/category/serateshgh/clip/" rel="category tag">کلیپ‌های دیگران</a></span>
	
</p>
					
					</li>
																		<li class="other-news tie_video">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211940/%d8%b9%d8%a7%d9%82%d8%a8%d8%aa-%d8%b1%da%98%db%8c%d9%85-%d8%a7%d8%b4%d8%ba%d8%a7%d9%84%da%af%d8%b1-%d9%82%d8%af%d8%b3/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/JUO2t_عاقبت-رژیم-اشغالگر-قدس-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211940/%d8%b9%d8%a7%d9%82%d8%a8%d8%aa-%d8%b1%da%98%db%8c%d9%85-%d8%a7%d8%b4%d8%ba%d8%a7%d9%84%da%af%d8%b1-%d9%82%d8%af%d8%b3/" rel="bookmark">عاقبت رژیم اشغالگر قدس</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/abas_ghre_daghi/" title="">عباس قره داغی </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>19 ساعت قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/clip/" rel="category tag">کلیپ‌های دیگران</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/212043/%d9%85%d8%a7%d8%af%d8%b1-%d8%b4%d9%87%db%8c%d8%af-%d8%a7%d8%a8%d8%b1%d8%a7%d9%87%db%8c%d9%85-%d8%a7%d9%84%d9%86%d8%a7%d8%a8%d9%84%d8%b3%db%8c-%d9%be%d8%b3%d8%b1%d9%85-%d9%be%db%8c%d8%b1%d9%88%d8%b2/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/166002708583882600-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" srcset="http://serateshgh.com/farsi/wp-content/uploads/2022/08/166002708583882600-110x75.jpg 110w, http://serateshgh.com/farsi/wp-content/uploads/2022/08/166002708583882600-300x201.jpg 300w, http://serateshgh.com/farsi/wp-content/uploads/2022/08/166002708583882600.jpg 471w" sizes="(max-width: 110px) 100vw, 110px" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/212043/%d9%85%d8%a7%d8%af%d8%b1-%d8%b4%d9%87%db%8c%d8%af-%d8%a7%d8%a8%d8%b1%d8%a7%d9%87%db%8c%d9%85-%d8%a7%d9%84%d9%86%d8%a7%d8%a8%d9%84%d8%b3%db%8c-%d9%be%d8%b3%d8%b1%d9%85-%d9%be%db%8c%d8%b1%d9%88%d8%b2/" rel="bookmark">مادر شهید ابراهیم النابلسی: پسرم پیروز شد</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/hannan_26/" title="">حنان </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>19 ساعت قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/212040/%d8%a8%d8%a7%d8%b2%d8%aa%d8%a7%d8%a8-%d8%a7%d9%82%d8%aa%d8%af%d8%a7%d8%b1-%d9%85%d8%a7%d9%87%d9%88%d8%a7%d8%b1%d9%87%e2%80%8c%d8%a7%db%8c-%d8%a7%db%8c%d8%b1%d8%a7%d9%86-%d8%af%d8%b1-%d8%b1%d8%b3%d8%a7/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/636213011118529253s-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/212040/%d8%a8%d8%a7%d8%b2%d8%aa%d8%a7%d8%a8-%d8%a7%d9%82%d8%aa%d8%af%d8%a7%d8%b1-%d9%85%d8%a7%d9%87%d9%88%d8%a7%d8%b1%d9%87%e2%80%8c%d8%a7%db%8c-%d8%a7%db%8c%d8%b1%d8%a7%d9%86-%d8%af%d8%b1-%d8%b1%d8%b3%d8%a7/" rel="bookmark">بازتاب اقتدار ماهواره‌ای ایران در رسانه‌های جهان</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/arash_86/" title="">آرش </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>19 ساعت قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/212037/%d8%b1%d8%b2%d9%85%d9%86%d8%af%d9%87-%d9%81%d8%a7%d8%b7%d9%85%db%8c%d9%88%d9%86-%da%a9%d9%87-%d8%a8%d8%a7-%d8%b4%d9%87%d8%a7%d8%af%d8%aa%d8%b4-%d8%a8%d8%b3%d8%aa%da%af%d8%a7%d9%86%d8%b4-%d8%b1%d8%a7/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/download-8-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/212037/%d8%b1%d8%b2%d9%85%d9%86%d8%af%d9%87-%d9%81%d8%a7%d8%b7%d9%85%db%8c%d9%88%d9%86-%da%a9%d9%87-%d8%a8%d8%a7-%d8%b4%d9%87%d8%a7%d8%af%d8%aa%d8%b4-%d8%a8%d8%b3%d8%aa%da%af%d8%a7%d9%86%d8%b4-%d8%b1%d8%a7/" rel="bookmark">رزمنده فاطمیون که با شهادتش بستگانش را مدافع حرم کرد</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/hannan_26/" title="">حنان </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>19 ساعت قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/212031/%db%8c%da%a9-%d8%b3%d8%a6%d9%88%d8%a7%d9%84-%d8%a7%d8%b2-%d8%b9%d9%84%db%8c-%da%a9%d8%b1%db%8c%d9%85%db%8c-%da%a9%d9%87-%d8%af%d8%b1%d8%a8%d8%a7%d8%b1%d9%87-%d9%86%d8%b0%d8%b1%db%8c-%d9%85%d8%ad%d8%b1/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/13980621000025_Test_PhotoN-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/212031/%db%8c%da%a9-%d8%b3%d8%a6%d9%88%d8%a7%d9%84-%d8%a7%d8%b2-%d8%b9%d9%84%db%8c-%da%a9%d8%b1%db%8c%d9%85%db%8c-%da%a9%d9%87-%d8%af%d8%b1%d8%a8%d8%a7%d8%b1%d9%87-%d9%86%d8%b0%d8%b1%db%8c-%d9%85%d8%ad%d8%b1/" rel="bookmark">یک سئوال از علی کریمی که درباره نذری محرم شبهه می‌اندازد</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/gilan_53/" title="">گیلان </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>20 ساعت قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/212028/%d8%b9%d9%84%d8%aa-%d8%aa%d9%88%d9%87%db%8c%d9%86-%d9%85%db%8c%d8%b1%d8%ad%d8%b3%db%8c%d9%86-%d9%85%d9%88%d8%b3%d9%88%db%8c-%d8%a8%d9%87-%d8%b4%d9%87%d8%af%d8%a7%db%8c-%d9%86%db%8c%d8%b1%d9%88%db%8c/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/download-7-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/212028/%d8%b9%d9%84%d8%aa-%d8%aa%d9%88%d9%87%db%8c%d9%86-%d9%85%db%8c%d8%b1%d8%ad%d8%b3%db%8c%d9%86-%d9%85%d9%88%d8%b3%d9%88%db%8c-%d8%a8%d9%87-%d8%b4%d9%87%d8%af%d8%a7%db%8c-%d9%86%db%8c%d8%b1%d9%88%db%8c/" rel="bookmark">علت توهین میرحسین موسوی به شهدای نیروی قدس و مدافعان حرم چیست؟</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/asieh_75/" title="">آسیه </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>20 ساعت قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/212027/%d8%a7%d8%b3%d9%85%d8%a7%d8%b9%db%8c%d9%84-%d8%a2%d8%b0%d8%b1-%d9%82%d8%b5%d9%87%e2%80%8c%da%af%d9%88%db%8c%db%8c-%d8%af%d8%b1-%d8%b2%d9%85%d8%a7%d9%86-%d9%86%d8%a7%d8%b5%d8%b1%d8%a7%d9%84%d8%af/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/13980617000604_Test_PhotoN-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/212027/%d8%a7%d8%b3%d9%85%d8%a7%d8%b9%db%8c%d9%84-%d8%a2%d8%b0%d8%b1-%d9%82%d8%b5%d9%87%e2%80%8c%da%af%d9%88%db%8c%db%8c-%d8%af%d8%b1-%d8%b2%d9%85%d8%a7%d9%86-%d9%86%d8%a7%d8%b5%d8%b1%d8%a7%d9%84%d8%af/" rel="bookmark">اسماعیل آذر: قصه‌گویی در زمان ناصرالدین‌شاه، منصب مهمی بود</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/khadije/" title="">خدیجه </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>20 ساعت قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/212011/%d8%a7%d8%b2-%d8%af%d8%b1%d8%b3%e2%80%8c%d9%87%d8%a7%db%8c-%d8%b9%d8%a7%d8%b4%d9%88%d8%b1%d8%a7-%d9%85%d9%87%d9%85%e2%80%8c%d8%aa%d8%b1%d8%8c-%d8%b9%d8%a8%d8%b1%d8%aa%e2%80%8c%d9%87%d8%a7%db%8c/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/1398102517172829719418244-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/212011/%d8%a7%d8%b2-%d8%af%d8%b1%d8%b3%e2%80%8c%d9%87%d8%a7%db%8c-%d8%b9%d8%a7%d8%b4%d9%88%d8%b1%d8%a7-%d9%85%d9%87%d9%85%e2%80%8c%d8%aa%d8%b1%d8%8c-%d8%b9%d8%a8%d8%b1%d8%aa%e2%80%8c%d9%87%d8%a7%db%8c/" rel="bookmark">از درس‌های عاشورا مهم‌تر، «عبرت‌های عاشورا» است/ اگر «خواص طرفدار حق» در اکثریت باشند جامعه تا ابد بیمه خواهد شد</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/daryoosh_32/" title="">داریوش </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>20 ساعت قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/212024/%d8%ac%d9%88%da%a9%d8%a7%d8%b1-%da%a9%d8%b3%d8%a7%d9%86%db%8c-%da%a9%d9%87-%d8%a8%d8%b1%d8%a7%db%8c-%d9%86%d8%b8%d8%a7%d9%85-%d9%87%d8%b2%db%8c%d9%86%d9%87-%d8%af%d8%b1%d8%b3%d8%aa-%da%a9%d8%b1%d8%af/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/14010414000992_Test_PhotoN-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/212024/%d8%ac%d9%88%da%a9%d8%a7%d8%b1-%da%a9%d8%b3%d8%a7%d9%86%db%8c-%da%a9%d9%87-%d8%a8%d8%b1%d8%a7%db%8c-%d9%86%d8%b8%d8%a7%d9%85-%d9%87%d8%b2%db%8c%d9%86%d9%87-%d8%af%d8%b1%d8%b3%d8%aa-%da%a9%d8%b1%d8%af/" rel="bookmark">جوکار: کسانی که برای نظام هزینه درست کردند به جای توبه بر طبل تفرقه می‌کوبند</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/arash_86/" title="">آرش </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>20 ساعت قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/212021/%d9%85%d8%b3%da%a9%d9%88-%d8%a7%db%8c%d8%af%d9%87%e2%80%8c%d9%87%d8%a7%db%8c-%d8%b2%d9%84%d9%86%d8%b3%da%a9%db%8c-%d9%87%d9%85%d8%a7%d9%86-%d8%a7%db%8c%d8%af%d9%87%e2%80%8c%d9%87%d8%a7%db%8c-%d9%87/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/n00153200-b-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/212021/%d9%85%d8%b3%da%a9%d9%88-%d8%a7%db%8c%d8%af%d9%87%e2%80%8c%d9%87%d8%a7%db%8c-%d8%b2%d9%84%d9%86%d8%b3%da%a9%db%8c-%d9%87%d9%85%d8%a7%d9%86-%d8%a7%db%8c%d8%af%d9%87%e2%80%8c%d9%87%d8%a7%db%8c-%d9%87/" rel="bookmark">مسکو: ایده‌های زلنسکی همان ایده‌های هیتلر است</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/msafr/" title="">مسافر </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>20 ساعت قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/212005/%d8%ab%d8%a8%d8%aa-%d8%b1%da%a9%d9%88%d8%b1%d8%af%e2%80%8c-%d8%b3%d8%a7%d8%ae%d8%aa-%d9%86%db%8c%d8%b1%d9%88%da%af%d8%a7%d9%87-%d8%af%d8%b1-%d8%a7%d9%88%d9%84%db%8c%d9%86-%d8%b3%d8%a7%d9%84-%d9%81/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/14010401000850_Test_PhotoN-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/212005/%d8%ab%d8%a8%d8%aa-%d8%b1%da%a9%d9%88%d8%b1%d8%af%e2%80%8c-%d8%b3%d8%a7%d8%ae%d8%aa-%d9%86%db%8c%d8%b1%d9%88%da%af%d8%a7%d9%87-%d8%af%d8%b1-%d8%a7%d9%88%d9%84%db%8c%d9%86-%d8%b3%d8%a7%d9%84-%d9%81/" rel="bookmark">ثبت رکورد‌ ساخت نیروگاه در اولین سال فعالیت دولت سیزدهم/ چرا تابستان امسال قطعی برق نداشتیم</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/gili_52/" title="">گیلی </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>20 ساعت قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211999/%d8%a2%d9%85%d8%a7%d8%b1-%d8%aa%da%a9%d8%a7%d9%86%e2%80%8c%d8%af%d9%87%d9%86%d8%af%d9%87-%d8%b3%d8%a7%d8%b2%d9%85%d8%a7%d9%86-%d9%85%d9%84%d9%84-%d8%a7%d8%b2-%d8%b4%d9%85%d8%a7%d8%b1-%da%a9%d9%88/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/310964-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211999/%d8%a2%d9%85%d8%a7%d8%b1-%d8%aa%da%a9%d8%a7%d9%86%e2%80%8c%d8%af%d9%87%d9%86%d8%af%d9%87-%d8%b3%d8%a7%d8%b2%d9%85%d8%a7%d9%86-%d9%85%d9%84%d9%84-%d8%a7%d8%b2-%d8%b4%d9%85%d8%a7%d8%b1-%da%a9%d9%88/" rel="bookmark">آمار تکان‌دهنده سازمان ملل از شمار کودکان و نوجوانانی که صهیونیست‌ها کشته‌اند</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/msafr/" title="">مسافر </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>20 ساعت قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/212010/%d8%af%d9%88%d9%84%d8%aa-%d8%b3%db%8c%d8%b2%d8%af%d9%87%d9%85-%da%86%da%af%d9%88%d9%86%d9%87-%d8%ae%d8%a7%d9%85%d9%88%d8%b4%db%8c%e2%80%8c%d9%87%d8%a7-%d8%b1%d8%a7-%d9%85%d8%aa%d9%88%d9%82%d9%81/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/169787913-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/212010/%d8%af%d9%88%d9%84%d8%aa-%d8%b3%db%8c%d8%b2%d8%af%d9%87%d9%85-%da%86%da%af%d9%88%d9%86%d9%87-%d8%ae%d8%a7%d9%85%d9%88%d8%b4%db%8c%e2%80%8c%d9%87%d8%a7-%d8%b1%d8%a7-%d9%85%d8%aa%d9%88%d9%82%d9%81/" rel="bookmark">دولت سیزدهم چگونه خاموشی‌ها را متوقف کرد؟</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/gilan_53/" title="">گیلان </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>20 ساعت قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/212000/%d8%ad%d8%a7%d9%85%d8%af-%da%a9%d8%b1%d8%b2%d8%a7%db%8c-%d8%a2%d9%85%d8%b1%db%8c%da%a9%d8%a7-%d9%85%d8%b1%d8%af%d9%85-%d8%a7%d9%81%d8%ba%d8%a7%d9%86%d8%b3%d8%aa%d8%a7%d9%86-%e2%80%8c%d8%b1%d8%a7/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/5581304-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/212000/%d8%ad%d8%a7%d9%85%d8%af-%da%a9%d8%b1%d8%b2%d8%a7%db%8c-%d8%a2%d9%85%d8%b1%db%8c%da%a9%d8%a7-%d9%85%d8%b1%d8%af%d9%85-%d8%a7%d9%81%d8%ba%d8%a7%d9%86%d8%b3%d8%aa%d8%a7%d9%86-%e2%80%8c%d8%b1%d8%a7/" rel="bookmark">حامد کرزای: آمریکا مردم افغانستان ‌را به‌عمد می‌کشت!</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/hamsayeh_36/" title="">همسایه </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>20 ساعت قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211968/%da%a9%d8%b1%d8%a8%d9%84%d8%a7-%d8%af%d8%b1-%da%a9%d8%b1%d8%a8%d9%84%d8%a7-%d9%86%d9%85%d8%a7%d9%86%d8%af/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/61721935-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211968/%da%a9%d8%b1%d8%a8%d9%84%d8%a7-%d8%af%d8%b1-%da%a9%d8%b1%d8%a8%d9%84%d8%a7-%d9%86%d9%85%d8%a7%d9%86%d8%af/" rel="bookmark">کربلا در کربلا نماند</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/hannan_26/" title="">حنان </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>20 ساعت قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211991/%d8%ba%d8%b0%d8%a7%d8%b1%d8%b3%d8%a7%d9%86%db%8c-%d8%a8%d9%87-%d8%b3%da%af%e2%80%8c%d9%87%d8%a7-%d8%b9%d8%a7%d9%85%d9%84-%d8%b1%d8%b4%d8%af-%d9%86%d8%ac%d9%88%d9%85%db%8c-%d9%86%d8%b1%d8%ae-%d8%b2/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/140010061328489324365624-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211991/%d8%ba%d8%b0%d8%a7%d8%b1%d8%b3%d8%a7%d9%86%db%8c-%d8%a8%d9%87-%d8%b3%da%af%e2%80%8c%d9%87%d8%a7-%d8%b9%d8%a7%d9%85%d9%84-%d8%b1%d8%b4%d8%af-%d9%86%d8%ac%d9%88%d9%85%db%8c-%d9%86%d8%b1%d8%ae-%d8%b2/" rel="bookmark">غذارسانی به سگ‌ها عامل رشد نجومی نرخ زادآوری آن‌هاست/ تعداد سگ‌های ولگرد از مرز ۲ میلیون گذشته است</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/gholam_47/" title="">غلام </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>20 ساعت قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211988/%d8%aa%d8%a3%da%a9%db%8c%d8%af-%d8%b5%d8%b1%db%8c%d8%ad-%d8%b1%d8%ac%d8%a8-%d8%b7%db%8c%d8%a8-%d8%a7%d8%b1%d8%af%d9%88%d8%ba%d8%a7%d9%86-%d8%a8%d8%b1-%d8%a7%d8%b4%d8%ba%d8%a7%d9%84%da%af%d8%b1%db%8c/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/1107008-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211988/%d8%aa%d8%a3%da%a9%db%8c%d8%af-%d8%b5%d8%b1%db%8c%d8%ad-%d8%b1%d8%ac%d8%a8-%d8%b7%db%8c%d8%a8-%d8%a7%d8%b1%d8%af%d9%88%d8%ba%d8%a7%d9%86-%d8%a8%d8%b1-%d8%a7%d8%b4%d8%ba%d8%a7%d9%84%da%af%d8%b1%db%8c/" rel="bookmark">تأکید صریح رجب طیب اردوغان بر اشغالگری در سوریه!</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/msafr/" title="">مسافر </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>20 ساعت قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211985/%d9%86%d8%ae%d8%b3%d8%aa%e2%80%8c%d9%88%d8%b2%db%8c%d8%b1-%d8%a7%d8%b3%d8%a8%d9%82-%d8%a7%d9%86%da%af%d9%84%db%8c%d8%b3-%d8%ae%d8%b7%d8%a7%d8%a8-%d8%a8%d9%87-%d9%85%d8%b1%d8%af%d9%85-%d8%a7%d9%86/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/2895834-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211985/%d9%86%d8%ae%d8%b3%d8%aa%e2%80%8c%d9%88%d8%b2%db%8c%d8%b1-%d8%a7%d8%b3%d8%a8%d9%82-%d8%a7%d9%86%da%af%d9%84%db%8c%d8%b3-%d8%ae%d8%b7%d8%a7%d8%a8-%d8%a8%d9%87-%d9%85%d8%b1%d8%af%d9%85-%d8%a7%d9%86/" rel="bookmark">نخست‌وزیر اسبق انگلیس خطاب به مردم انگلیس: «منتظر گرسنگی و سرما باشید»</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/msafr/" title="">مسافر </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>20 ساعت قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211994/%d8%aa%da%a9%d8%b1%d8%a7%d8%b1-%da%a9%d8%b4%d8%aa%d8%a7%d8%b1-%d8%b9%d8%b2%d8%a7%d8%af%d8%a7%d8%b1%d8%a7%d9%86-%d9%85%d8%b8%d9%84%d9%88%d9%85-%d8%a7%d9%85%d8%a7%d9%85-%d8%ad%d8%b3%db%8c%d9%86%e2%80%8c/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/download-6-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211994/%d8%aa%da%a9%d8%b1%d8%a7%d8%b1-%da%a9%d8%b4%d8%aa%d8%a7%d8%b1-%d8%b9%d8%b2%d8%a7%d8%af%d8%a7%d8%b1%d8%a7%d9%86-%d9%85%d8%b8%d9%84%d9%88%d9%85-%d8%a7%d9%85%d8%a7%d9%85-%d8%ad%d8%b3%db%8c%d9%86%e2%80%8c/" rel="bookmark">تکرار کشتار عزاداران مظلوم امام حسین‌(علیه السلام) در نیجریه</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/hamsayeh_36/" title="">همسایه </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>20 ساعت قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211979/%d8%aa%d8%ac%d9%85%d8%b9-%d8%b6%d8%af%d8%b5%d9%87%db%8c%d9%88%d9%86%db%8c%d8%b3%d8%aa%db%8c-%d9%85%d8%b1%d8%af%d9%85-%d8%b9%d8%a7%d8%b4%d9%88%d8%b1%d8%a7%db%8c%db%8c-%d8%aa%d9%87%d8%b1%d8%a7%d9%86/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/165998325581706000-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211979/%d8%aa%d8%ac%d9%85%d8%b9-%d8%b6%d8%af%d8%b5%d9%87%db%8c%d9%88%d9%86%db%8c%d8%b3%d8%aa%db%8c-%d9%85%d8%b1%d8%af%d9%85-%d8%b9%d8%a7%d8%b4%d9%88%d8%b1%d8%a7%db%8c%db%8c-%d8%aa%d9%87%d8%b1%d8%a7%d9%86/" rel="bookmark">تجمع ضدصهیونیستی مردم عاشورایی تهران در میدان فلسطین برگزار شد</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/arash_86/" title="">آرش </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>21 ساعت قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211973/%da%a9%db%8c%d8%a7%d9%86%db%8c-%d8%af%d8%ae%d8%aa%d8%b1-%d8%aa%da%a9%d9%88%d8%a7%d9%86%d8%af%d9%88%db%8c-%d8%a7%db%8c%d8%b1%d8%a7%d9%86%d8%8c-%d8%a7%d9%88%d9%84%db%8c%d9%86-%d8%b7%d9%84%d8%a7%db%8c/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/2461846-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211973/%da%a9%db%8c%d8%a7%d9%86%db%8c-%d8%af%d8%ae%d8%aa%d8%b1-%d8%aa%da%a9%d9%88%d8%a7%d9%86%d8%af%d9%88%db%8c-%d8%a7%db%8c%d8%b1%d8%a7%d9%86%d8%8c-%d8%a7%d9%88%d9%84%db%8c%d9%86-%d8%b7%d9%84%d8%a7%db%8c/" rel="bookmark">کیانی دختر تکواندوی ایران، اولین طلای بانوان را ضرب کرد</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/ameneh_43/" title="">آمنه </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>21 ساعت قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211984/%d8%a7%d8%af%d8%b9%d8%a7%db%8c-%d8%a8%db%8c-%d9%be%d8%a7%db%8c%d9%87-%d9%81%d8%a7%d8%b7%d9%85%d9%87-%d9%87%d8%a7%d8%b4%d9%85%db%8c-%d8%b9%d9%84%db%8c%d9%87-%d9%82%d8%a7%d9%86%d9%88%d9%86/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/original-e1660087485449-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211984/%d8%a7%d8%af%d8%b9%d8%a7%db%8c-%d8%a8%db%8c-%d9%be%d8%a7%db%8c%d9%87-%d9%81%d8%a7%d8%b7%d9%85%d9%87-%d9%87%d8%a7%d8%b4%d9%85%db%8c-%d8%b9%d9%84%db%8c%d9%87-%d9%82%d8%a7%d9%86%d9%88%d9%86/" rel="bookmark">ادعای بی پایه «فاطمه هاشمی» علیه قانون«جوانی جمعیت» نتیجه کم سوادی یا &#8230;؟!</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/somayyeh_94/" title="">سمیه </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>21 ساعت قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211974/%d8%a8%d9%87-%d8%a7%d9%86%da%af%db%8c%d8%b2%d9%87-%d8%b4%d9%87%d8%a7%d8%af%d8%aa-%d8%ac%d8%a7%d9%86%d8%b3%d9%88%d8%b2-%d8%a7%d9%85%d8%a7%d9%85-%d8%b3%d8%ac%d9%91%d8%a7%d8%af-%d8%b9%d9%84%db%8c%d9%87/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/13930311_0126571-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211974/%d8%a8%d9%87-%d8%a7%d9%86%da%af%db%8c%d8%b2%d9%87-%d8%b4%d9%87%d8%a7%d8%af%d8%aa-%d8%ac%d8%a7%d9%86%d8%b3%d9%88%d8%b2-%d8%a7%d9%85%d8%a7%d9%85-%d8%b3%d8%ac%d9%91%d8%a7%d8%af-%d8%b9%d9%84%db%8c%d9%87/" rel="bookmark">به انگیزه شهادت جانسوز امام سجّاد علیه‌السلام</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/hannan_26/" title="">حنان </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>21 ساعت قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211965/%d8%a2%d9%82%d8%a7%db%8c%d8%a7%d9%86-%d9%85%d8%af%d8%b9%db%8c-%d8%a7%d8%b5%d9%84%d8%a7%d8%ad%d8%a7%d8%aa-%d8%a8%d8%a7%d8%ac-%d8%b1%d8%a7-%d8%aa%d9%88%d8%a7%d9%81%d9%82-%d8%aa%d8%b1%d8%ac%d9%85%d9%87/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/110107-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211965/%d8%a2%d9%82%d8%a7%db%8c%d8%a7%d9%86-%d9%85%d8%af%d8%b9%db%8c-%d8%a7%d8%b5%d9%84%d8%a7%d8%ad%d8%a7%d8%aa-%d8%a8%d8%a7%d8%ac-%d8%b1%d8%a7-%d8%aa%d9%88%d8%a7%d9%81%d9%82-%d8%aa%d8%b1%d8%ac%d9%85%d9%87/" rel="bookmark">آقایان مدعی اصلاحات باج را توافق ترجمه نکنید!</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/h_shariatmadari_73/" title="">حسین شریعتمداری </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>21 ساعت قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211964/%d9%85%d8%a3%d9%85%d9%88%d8%b1%db%8c%d8%aa-%d8%af%db%8c%da%a9%d8%aa%d9%87%e2%80%8c%d8%b4%d8%af%d9%87-%db%8c%da%a9%db%8c-%d8%a7%d8%b2-%d8%b3%d8%b1%d8%a7%d9%86-%d9%81%d8%aa%d9%86%d9%87-%d8%af%d8%b1/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/13941009000091_PhotoL-e1660086917742-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211964/%d9%85%d8%a3%d9%85%d9%88%d8%b1%db%8c%d8%aa-%d8%af%db%8c%da%a9%d8%aa%d9%87%e2%80%8c%d8%b4%d8%af%d9%87-%db%8c%da%a9%db%8c-%d8%a7%d8%b2-%d8%b3%d8%b1%d8%a7%d9%86-%d9%81%d8%aa%d9%86%d9%87-%d8%af%d8%b1/" rel="bookmark">مأموریت دیکته‌شده یکی از سران فتنه در حمایت آشکار از اسرائیل و داعش</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/gholam_47/" title="">غلام </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>21 ساعت قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news tie_video">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211946/%d8%ad%d8%b0%d9%81-%da%af%d8%b4%d8%aa-%d8%a7%d8%b1%d8%b4%d8%a7%d8%af-%d8%af%d8%b1-%d9%86%da%af%d8%a7%d9%87-%d8%a2%d9%82%d8%a7%db%8c-%d8%b1%d8%ad%db%8c%d9%85-%d9%be%d9%88%d8%b1%d8%a7%d8%b2%d8%ba%d8%af/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/06/57727922-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211946/%d8%ad%d8%b0%d9%81-%da%af%d8%b4%d8%aa-%d8%a7%d8%b1%d8%b4%d8%a7%d8%af-%d8%af%d8%b1-%d9%86%da%af%d8%a7%d9%87-%d8%a2%d9%82%d8%a7%db%8c-%d8%b1%d8%ad%db%8c%d9%85-%d9%be%d9%88%d8%b1%d8%a7%d8%b2%d8%ba%d8%af/" rel="bookmark">حذف گشت ارشاد در نگاه آقای رحیم پورازغدی</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/abas_ghre_daghi/" title="">عباس قره داغی </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>21 ساعت قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/clip/" rel="category tag">کلیپ‌های دیگران</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211960/%d8%a7%d8%b7%d9%84%d8%a7%d8%b9%d8%a7%d8%aa-%d9%85%d8%ad%d8%b1%d9%85%d8%a7%d9%86%d9%87-%d8%af%d8%b1-%d8%ac%db%8c%d8%a8-%d8%af%d9%88%d8%aa%d8%a7%d8%a8%d8%b9%db%8c%d8%aa%db%8c%e2%80%8c%d9%87%d8%a7%db%8c/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/download-5-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211960/%d8%a7%d8%b7%d9%84%d8%a7%d8%b9%d8%a7%d8%aa-%d9%85%d8%ad%d8%b1%d9%85%d8%a7%d9%86%d9%87-%d8%af%d8%b1-%d8%ac%db%8c%d8%a8-%d8%af%d9%88%d8%aa%d8%a7%d8%a8%d8%b9%db%8c%d8%aa%db%8c%e2%80%8c%d9%87%d8%a7%db%8c/" rel="bookmark">اطلاعات محرمانه در جیب دوتابعیتی‌های اتاق بازرگانی</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/gili_52/" title="">گیلی </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>22 ساعت قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news tie_video">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211937/%d8%a8%d8%a7%d8%a8-%d8%a7%d9%84%d8%ad%d8%b3%db%8c%d9%86-%da%af%d8%b1%d9%88%d9%87-%d8%b3%d8%b1%d9%88%d8%af-%d8%a8%da%86%d9%87-%d9%87%d8%a7%db%8c-%d8%a2%d8%b3%d9%85%d8%a7%d9%86/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/i1fp2_باب-الحسین-گروه-سرود-بچه-های-آسمان-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211937/%d8%a8%d8%a7%d8%a8-%d8%a7%d9%84%d8%ad%d8%b3%db%8c%d9%86-%da%af%d8%b1%d9%88%d9%87-%d8%b3%d8%b1%d9%88%d8%af-%d8%a8%da%86%d9%87-%d9%87%d8%a7%db%8c-%d8%a2%d8%b3%d9%85%d8%a7%d9%86/" rel="bookmark">باب الحسین (گروه سرود بچه های آسمان)</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/abas_ghre_daghi/" title="">عباس قره داغی </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>22 ساعت قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/clip/" rel="category tag">کلیپ‌های دیگران</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211954/%d9%87%d9%85%da%a9%d8%a7%d8%b1%db%8c-%d9%81%d8%b6%d8%a7%db%8c%db%8c-%d8%a7%db%8c%d8%b1%d8%a7%d9%86-%d9%88-%d8%b1%d9%88%d8%b3%db%8c%d9%87-%d8%b1%d8%b5%d8%af-%d8%b2%d9%85%db%8c%d9%86-%d8%a8%d8%a7-%d8%af/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/1294796_187-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211954/%d9%87%d9%85%da%a9%d8%a7%d8%b1%db%8c-%d9%81%d8%b6%d8%a7%db%8c%db%8c-%d8%a7%db%8c%d8%b1%d8%a7%d9%86-%d9%88-%d8%b1%d9%88%d8%b3%db%8c%d9%87-%d8%b1%d8%b5%d8%af-%d8%b2%d9%85%db%8c%d9%86-%d8%a8%d8%a7-%d8%af/" rel="bookmark">همکاری فضایی ایران و روسیه رصد زمین با دقت یک متر</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/arash_86/" title="">آرش </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>22 ساعت قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211932/%db%8c%da%a9-%d8%b2%d9%86-%d8%a7%d9%87%d9%84-%d8%b3%d9%86%d8%aa-%d9%85%d9%88%d8%b5%d9%84-%d8%af%d8%b1-%d8%b4%d8%a8%da%a9%d9%87-%d9%87%d8%a7%db%8c-%d8%a7%d8%ac%d8%aa%d9%85%d8%a7%d8%b9%db%8c-%d8%b9/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/168876108-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211932/%db%8c%da%a9-%d8%b2%d9%86-%d8%a7%d9%87%d9%84-%d8%b3%d9%86%d8%aa-%d9%85%d9%88%d8%b5%d9%84-%d8%af%d8%b1-%d8%b4%d8%a8%da%a9%d9%87-%d9%87%d8%a7%db%8c-%d8%a7%d8%ac%d8%aa%d9%85%d8%a7%d8%b9%db%8c-%d8%b9/" rel="bookmark">یک زن اهل سنت موصل در شبکه های اجتماعی عراق نوشت</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/zarin_99/" title="">مهندس رضا زرین </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>1 روز قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a>, <a href="http://serateshgh.com/category/serateshgh/art/%d8%b9%da%a9%d8%b3-%d9%88-%da%af%d8%b1%d8%a7%d9%81%db%8c%da%a9-%d8%af%db%8c%da%af%d8%b1%d8%a7%d9%86/" rel="category tag">عکس و گرافیک دیگران</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211924/%da%a9%d8%a7%d8%b1%d9%88%d8%a7%d9%86-%d8%ad%d8%b3%db%8c%d9%86%db%8c-%d8%a8%d8%a7-%d8%b1%d8%ac%d8%b9%d8%aa%d8%b4%d8%a7%d9%86-%d9%85%d8%a3%d9%85%d9%88%d8%b1%db%8c%d8%aa-%d8%ae%d9%88%d8%af-%d8%b1%d8%a7/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/download-4-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211924/%da%a9%d8%a7%d8%b1%d9%88%d8%a7%d9%86-%d8%ad%d8%b3%db%8c%d9%86%db%8c-%d8%a8%d8%a7-%d8%b1%d8%ac%d8%b9%d8%aa%d8%b4%d8%a7%d9%86-%d9%85%d8%a3%d9%85%d9%88%d8%b1%db%8c%d8%aa-%d8%ae%d9%88%d8%af-%d8%b1%d8%a7/" rel="bookmark">کاروان حسینی با رجعتشان مأموریت خود را تکامل می‌بخشند</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/arash_86/" title="">آرش </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>1 روز قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211925/%d8%b4%d9%87%db%8c%d8%af-%d8%ae%d8%b1%d8%a7%d8%b2%db%8c-%d9%87%db%8c%d9%87%d8%a7%d8%aa-%d9%85%d9%86%d9%91%d8%a7-%d8%a7%d9%84%d8%b0%d9%91%d9%84%d9%87%d8%8c-%db%8c%d8%b9%d9%86%db%8c-%d8%aa%d9%86-%d9%86/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/1396120514302882113439864-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211925/%d8%b4%d9%87%db%8c%d8%af-%d8%ae%d8%b1%d8%a7%d8%b2%db%8c-%d9%87%db%8c%d9%87%d8%a7%d8%aa-%d9%85%d9%86%d9%91%d8%a7-%d8%a7%d9%84%d8%b0%d9%91%d9%84%d9%87%d8%8c-%db%8c%d8%b9%d9%86%db%8c-%d8%aa%d9%86-%d9%86/" rel="bookmark">شهید خرازی: هیهات منّا الذّله، یعنی تن ندادن به ذلت و تسلیم</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/hannan_26/" title="">حنان </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>1 روز قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211909/%d8%ac%d9%87%d8%a7%d8%af-%d8%af%d8%b1-%d8%a7%d9%81%d8%ba%d8%a7%d9%86%d8%b3%d8%aa%d8%a7%d9%86-%d8%a8%d8%b1%d8%a7%db%8c-%d8%b4%d9%87%db%8c%d8%af-%d9%85%d8%b5%d8%b7%d9%81%db%8c-%d8%ac%d8%b9%d9%81%d8%b1/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/14010517000231_Test_PhotoN-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211909/%d8%ac%d9%87%d8%a7%d8%af-%d8%af%d8%b1-%d8%a7%d9%81%d8%ba%d8%a7%d9%86%d8%b3%d8%aa%d8%a7%d9%86-%d8%a8%d8%b1%d8%a7%db%8c-%d8%b4%d9%87%db%8c%d8%af-%d9%85%d8%b5%d8%b7%d9%81%db%8c-%d8%ac%d8%b9%d9%81%d8%b1/" rel="bookmark">جهاد در افغانستان برای شهید مصطفی جعفری کافی نبود</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/hannan_26/" title="">حنان </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>1 روز قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211913/%d8%b1%d9%88%d8%b6%d9%87%e2%80%8c%d8%ae%d9%88%d8%a7%d9%86%db%8c-%d9%85%d8%ad%d9%85%d9%88%d8%af-%da%a9%d8%b1%db%8c%d9%85%db%8c-%d8%af%d8%b1-%d8%ae%d8%a7%d9%86%d9%87-%d8%ad%d8%a7%d8%ac-%d9%82%d8%a7/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/1549853-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211913/%d8%b1%d9%88%d8%b6%d9%87%e2%80%8c%d8%ae%d9%88%d8%a7%d9%86%db%8c-%d9%85%d8%ad%d9%85%d9%88%d8%af-%da%a9%d8%b1%db%8c%d9%85%db%8c-%d8%af%d8%b1-%d8%ae%d8%a7%d9%86%d9%87-%d8%ad%d8%a7%d8%ac-%d9%82%d8%a7/" rel="bookmark">روضه‌خوانی محمود کریمی در خانه حاج قاسم سلیمانی +فیلم</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/hannan_26/" title="">حنان </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>1 روز قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211912/%d8%b1%d8%ac%d8%b2-%d9%81%d8%a7%d8%b1%d8%b3%db%8c%d8%8c-%d8%b9%d8%b1%d8%a8%db%8c%d8%8c-%d8%b9%d8%a8%d8%b1%db%8c-%d9%85%db%8c%d8%ab%d9%85-%d9%85%d8%b7%db%8c%d8%b9%db%8c-%d8%b9%d9%84%db%8c%d9%87-%d8%b1/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/14010516000333_Test_PhotoN-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211912/%d8%b1%d8%ac%d8%b2-%d9%81%d8%a7%d8%b1%d8%b3%db%8c%d8%8c-%d8%b9%d8%b1%d8%a8%db%8c%d8%8c-%d8%b9%d8%a8%d8%b1%db%8c-%d9%85%db%8c%d8%ab%d9%85-%d9%85%d8%b7%db%8c%d8%b9%db%8c-%d8%b9%d9%84%db%8c%d9%87-%d8%b1/" rel="bookmark">رجز فارسی، عربی، عبری میثم مطیعی علیه رژیم صهیونیستی +فیلم</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/nariman_76/" title="">نریمان </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>1 روز قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news tie_none">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211895/%d9%be%d9%88%d8%b3%d8%aa%d8%b1-%d8%a7%db%8c%d9%86-%d8%a7%d9%84%d9%85%d9%86%d8%aa%d9%82%d9%85/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/236004600_342489394278932_8693120107920319460_n2-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211895/%d9%be%d9%88%d8%b3%d8%aa%d8%b1-%d8%a7%db%8c%d9%86-%d8%a7%d9%84%d9%85%d9%86%d8%aa%d9%82%d9%85/" rel="bookmark">پوستر/ این المنتقم</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/hadi_mnghi_77/" title="">هادی منقی </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>1 روز قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/art/%d9%be%d9%88%d8%b3%d8%aa%d8%b1/" rel="category tag">پوستر</a>, <a href="http://serateshgh.com/category/serateshgh/art/" rel="category tag">هنر</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211911/%d8%a7%d9%88%d9%84%db%8c%d9%86-%d8%b1%d8%a6%db%8c%d8%b3%e2%80%8c%d8%ac%d9%85%d9%87%d9%88%d8%b1-%da%86%d9%be%da%af%d8%b1%d8%a7%db%8c-%d8%aa%d8%a7%d8%b1%db%8c%d8%ae-%da%a9%d9%84%d9%85%d8%a8%db%8c%d8%a7/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/169757171-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211911/%d8%a7%d9%88%d9%84%db%8c%d9%86-%d8%b1%d8%a6%db%8c%d8%b3%e2%80%8c%d8%ac%d9%85%d9%87%d9%88%d8%b1-%da%86%d9%be%da%af%d8%b1%d8%a7%db%8c-%d8%aa%d8%a7%d8%b1%db%8c%d8%ae-%da%a9%d9%84%d9%85%d8%a8%db%8c%d8%a7/" rel="bookmark">اولین رئیس‌جمهور چپگرای تاریخ کلمبیا سوگند خورد</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/msafr/" title="">مسافر </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>1 روز قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211884/%d8%aa%d8%b1%d9%88%db%8c%d8%ac-%d8%a7%d8%a8%d8%a7%d8%ad%d9%87%e2%80%8c%da%af%d8%b1%db%8c-%d8%a8%d8%a7-%d8%aa%d9%88%d8%b3%d9%84-%d8%a8%d9%87-%d9%85%d8%ba%d8%a7%d9%84%d8%b7%d9%87/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/file-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211884/%d8%aa%d8%b1%d9%88%db%8c%d8%ac-%d8%a7%d8%a8%d8%a7%d8%ad%d9%87%e2%80%8c%da%af%d8%b1%db%8c-%d8%a8%d8%a7-%d8%aa%d9%88%d8%b3%d9%84-%d8%a8%d9%87-%d9%85%d8%ba%d8%a7%d9%84%d8%b7%d9%87/" rel="bookmark">ترویج اباحه‌گری با توسل به مغالطه!</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/arash_86/" title="">آرش </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>1 روز قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211899/%d8%ae%d8%b4%da%a9%d8%b3%d8%a7%d9%84%db%8c-%d8%aa%d8%a7%d8%b1%db%8c%d8%ae%db%8c-%d8%af%d8%b1-%d8%a7%d8%b1%d9%88%d9%be%d8%a7-100-%d8%b4%d9%87%d8%b1-%d9%81%d8%b1%d8%a7%d9%86%d8%b3%d9%87-%d8%a2%d8%a8/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/164601426-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211899/%d8%ae%d8%b4%da%a9%d8%b3%d8%a7%d9%84%db%8c-%d8%aa%d8%a7%d8%b1%db%8c%d8%ae%db%8c-%d8%af%d8%b1-%d8%a7%d8%b1%d9%88%d9%be%d8%a7-100-%d8%b4%d9%87%d8%b1-%d9%81%d8%b1%d8%a7%d9%86%d8%b3%d9%87-%d8%a2%d8%a8/" rel="bookmark">خشکسالی تاریخی در اروپا  100 شهر فرانسه آب آشامیدنی ندارد</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/msafr/" title="">مسافر </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>1 روز قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211903/%d8%a8%db%8c%e2%80%8c%d8%ad%d8%ac%d8%a7%d8%a8%db%8c-%d8%a7%d8%ac%d8%a8%d8%a7%d8%b1%db%8c-%d8%af%d8%b1-%d9%81%d8%b1%d8%a7%d9%86%d8%b3%d9%87-%d8%b5%d8%af%d8%a7%db%8c-%d8%a7%d8%b9%d8%aa%d8%b1%d8%a7%d8%b6/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/1823110_771-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211903/%d8%a8%db%8c%e2%80%8c%d8%ad%d8%ac%d8%a7%d8%a8%db%8c-%d8%a7%d8%ac%d8%a8%d8%a7%d8%b1%db%8c-%d8%af%d8%b1-%d9%81%d8%b1%d8%a7%d9%86%d8%b3%d9%87-%d8%b5%d8%af%d8%a7%db%8c-%d8%a7%d8%b9%d8%aa%d8%b1%d8%a7%d8%b6/" rel="bookmark">بی‌حجابی اجباری در فرانسه صدای اعتراض سازمان ملل را هم درآورد</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/msafr/" title="">مسافر </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>1 روز قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211894/%d8%a7%db%8c%d9%86%d8%b3%d8%aa%d8%a7%da%af%d8%b1%d8%a7%d9%85-%d8%a7%d9%86%d8%aa%d8%b4%d8%a7%d8%b1-%d8%aa%d8%b5%d9%88%db%8c%d8%b1-%d8%b4%d9%87%db%8c%d8%af-5-%d8%b3%d8%a7%d9%84%d9%87-%d9%81%d9%84%d8%b3/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/357433-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211894/%d8%a7%db%8c%d9%86%d8%b3%d8%aa%d8%a7%da%af%d8%b1%d8%a7%d9%85-%d8%a7%d9%86%d8%aa%d8%b4%d8%a7%d8%b1-%d8%aa%d8%b5%d9%88%db%8c%d8%b1-%d8%b4%d9%87%db%8c%d8%af-5-%d8%b3%d8%a7%d9%84%d9%87-%d9%81%d9%84%d8%b3/" rel="bookmark">اینستاگرام انتشار تصویر شهید 5 ساله فلسطینی را ممنوع اعلام کرد!</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/hamsayeh_36/" title="">همسایه </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>1 روز قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211893/%d8%ae%d8%b7%d8%b1-%d8%aa%da%a9%d8%b1%d8%a7%d8%b1-%d9%81%d8%a7%d8%ac%d8%b9%d9%87-%d8%a7%db%8c-%d8%a8%d8%b2%d8%b1%da%af%e2%80%8c%d8%aa%d8%b1-%d8%a7%d8%b2-%da%86%d8%b1%d9%86%d9%88%d8%a8%db%8c%d9%84/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/download-3-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211893/%d8%ae%d8%b7%d8%b1-%d8%aa%da%a9%d8%b1%d8%a7%d8%b1-%d9%81%d8%a7%d8%ac%d8%b9%d9%87-%d8%a7%db%8c-%d8%a8%d8%b2%d8%b1%da%af%e2%80%8c%d8%aa%d8%b1-%d8%a7%d8%b2-%da%86%d8%b1%d9%86%d9%88%d8%a8%db%8c%d9%84/" rel="bookmark">خطر تکرار فاجعه ای بزرگ‌تر از چرنوبیل در بزرگ‌ترین نیروگاه اتمی اروپا</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/msafr/" title="">مسافر </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>1 روز قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211889/%d8%a2%d9%82%d8%a7%db%8c-%d8%b1%d9%88%d8%ad%d8%a7%d9%86%db%8c-%d8%a7%d9%88%d8%a8%d8%a7%d9%85%d8%a7-%d9%88-%d8%aa%d8%b1%d8%a7%d9%85%d9%be-%d9%be%d8%b4%d8%aa%da%af%d8%b1%d9%85-%d8%a8%d9%87-%d8%b4%d9%85/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/1754333_552-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211889/%d8%a2%d9%82%d8%a7%db%8c-%d8%b1%d9%88%d8%ad%d8%a7%d9%86%db%8c-%d8%a7%d9%88%d8%a8%d8%a7%d9%85%d8%a7-%d9%88-%d8%aa%d8%b1%d8%a7%d9%85%d9%be-%d9%be%d8%b4%d8%aa%da%af%d8%b1%d9%85-%d8%a8%d9%87-%d8%b4%d9%85/" rel="bookmark">آقای روحانی! اوباما و ترامپ پشتگرم به شما برجام را زیر پا گذاشتند</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/gholam_47/" title="">غلام </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>1 روز قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211885/%d8%b9%d8%b5%d8%a8%d8%a7%d9%86%db%8c%d8%aa-%d9%85%d8%af%d8%b9%db%8c%d8%a7%d9%86-%d8%a7%d8%b5%d9%84%d8%a7%d8%ad%d8%a7%d8%aa-%d8%a7%d8%b2-%da%af%d8%b2%d8%a7%d8%b1%d8%b4-%da%a9%db%8c%d9%87%d8%a7%d9%86/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/14010513000090_Test_PhotoN-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211885/%d8%b9%d8%b5%d8%a8%d8%a7%d9%86%db%8c%d8%aa-%d9%85%d8%af%d8%b9%db%8c%d8%a7%d9%86-%d8%a7%d8%b5%d9%84%d8%a7%d8%ad%d8%a7%d8%aa-%d8%a7%d8%b2-%da%af%d8%b2%d8%a7%d8%b1%d8%b4-%da%a9%db%8c%d9%87%d8%a7%d9%86/" rel="bookmark">عصبانیت مدعیان اصلاحات از گزارش کیهان درباره شبکه نیابتی دشمن</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/gilan_53/" title="">گیلان </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>1 روز قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211883/%d8%af%d9%88%d9%84%d8%aa-%d8%b3%db%8c%d8%b2%d8%af%d9%87%d9%85-%d8%af%d8%b1-%d8%aa%d8%a3%d9%85%db%8c%d9%86-%d8%a8%d8%b1%d9%82-%d8%aa%d8%a7%d8%a8%d8%b3%d8%aa%d8%a7%d9%86-%d8%af%d8%a7%d8%ba-%d8%a8%d8%af/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/107970_152-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211883/%d8%af%d9%88%d9%84%d8%aa-%d8%b3%db%8c%d8%b2%d8%af%d9%87%d9%85-%d8%af%d8%b1-%d8%aa%d8%a3%d9%85%db%8c%d9%86-%d8%a8%d8%b1%d9%82-%d8%aa%d8%a7%d8%a8%d8%b3%d8%aa%d8%a7%d9%86-%d8%af%d8%a7%d8%ba-%d8%a8%d8%af/" rel="bookmark">دولت سیزدهم در تأمین برق تابستان داغ بدون خاموشی</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/gili_52/" title="">گیلی </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>1 روز قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news tie_video">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211868/%d9%85%d8%af%d8%a7%d8%ad%db%8c-%d8%ac%d8%a7%d9%86%d8%a8%d8%a7%d8%b2-%d8%af%d9%88-%d8%af%d8%b3%d8%aa-%d9%82%d8%b7%d8%b9%d8%8c-%d8%af%d8%b1%d8%ad%d8%b3%db%8c%d9%86%db%8c%d9%87-%d9%85%d8%b9%d9%84%db%8c/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/جانباز-دو-دست-قطع،-درحسینیه-معلی-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211868/%d9%85%d8%af%d8%a7%d8%ad%db%8c-%d8%ac%d8%a7%d9%86%d8%a8%d8%a7%d8%b2-%d8%af%d9%88-%d8%af%d8%b3%d8%aa-%d9%82%d8%b7%d8%b9%d8%8c-%d8%af%d8%b1%d8%ad%d8%b3%db%8c%d9%86%db%8c%d9%87-%d9%85%d8%b9%d9%84%db%8c/" rel="bookmark">مداحی جانباز دو دست قطع، درحسینیه معلی</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/msavd_pvr_ali/" title="">مسعود پور علی </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>2 روز قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/clip/" rel="category tag">کلیپ‌های دیگران</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211875/%d9%85%d8%a7%d9%87%d9%88%d8%a7%d8%b1%d9%87-%d8%a7%db%8c%d8%b1%d8%a7%d9%86%db%8c-%d8%ae%db%8c%d8%a7%d9%85-%d9%be%d8%b1%d8%aa%d8%a7%d8%a8-%d8%b4%d8%af%d9%81%db%8c%d9%84%d9%85/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/14010518000243_Test_PhotoN-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211875/%d9%85%d8%a7%d9%87%d9%88%d8%a7%d8%b1%d9%87-%d8%a7%db%8c%d8%b1%d8%a7%d9%86%db%8c-%d8%ae%db%8c%d8%a7%d9%85-%d9%be%d8%b1%d8%aa%d8%a7%d8%a8-%d8%b4%d8%af%d9%81%db%8c%d9%84%d9%85/" rel="bookmark">ماهواره ایرانی خیام پرتاب شد+فیلم</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/arash_86/" title="">آرش </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>2 روز قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211878/%d9%be%db%8c%d8%b4%e2%80%8c%d8%a8%db%8c%d9%86%db%8c-%db%b6-%d9%85%d8%b1%d8%b2-%d8%a8%d8%b1%d8%a7%db%8c-%d8%aa%d8%b1%d8%af%d8%af-%d8%b2%d8%a7%d8%a6%d8%b1%d8%a7%d9%86-%d8%a7%d8%b1%d8%a8%d8%b9%db%8c/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/1022259-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211878/%d9%be%db%8c%d8%b4%e2%80%8c%d8%a8%db%8c%d9%86%db%8c-%db%b6-%d9%85%d8%b1%d8%b2-%d8%a8%d8%b1%d8%a7%db%8c-%d8%aa%d8%b1%d8%af%d8%af-%d8%b2%d8%a7%d8%a6%d8%b1%d8%a7%d9%86-%d8%a7%d8%b1%d8%a8%d8%b9%db%8c/" rel="bookmark">پیش‌بینی ۶ مرز برای تردد زائران اربعین حسینی</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/gilan_53/" title="">گیلان </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>2 روز قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211862/%d8%b9%d8%a7%d8%b4%d9%88%d8%b1%d8%a7%db%8c-%d8%ad%d8%b3%db%8c%d9%86%db%8c-%d8%a7%d8%b2-%da%a9%d8%b1%d8%a8%d9%84%d8%a7-%d9%88-%d9%85%d8%b2%d8%a7%d8%b1%d8%b4%d8%b1%db%8c%d9%81-%d9%88-%d8%b5%d9%86%d8%b9/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/15026390-1-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" srcset="http://serateshgh.com/farsi/wp-content/uploads/2022/08/15026390-1-110x75.jpg 110w, http://serateshgh.com/farsi/wp-content/uploads/2022/08/15026390-1-300x202.jpg 300w, http://serateshgh.com/farsi/wp-content/uploads/2022/08/15026390-1.jpg 720w" sizes="(max-width: 110px) 100vw, 110px" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211862/%d8%b9%d8%a7%d8%b4%d9%88%d8%b1%d8%a7%db%8c-%d8%ad%d8%b3%db%8c%d9%86%db%8c-%d8%a7%d8%b2-%da%a9%d8%b1%d8%a8%d9%84%d8%a7-%d9%88-%d9%85%d8%b2%d8%a7%d8%b1%d8%b4%d8%b1%db%8c%d9%81-%d9%88-%d8%b5%d9%86%d8%b9/" rel="bookmark">عاشورای حسینی از کربلا و مزارشریف و صنعا تا وین و نیویورک و کنیا</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/gholam_47/" title="">غلام </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>2 روز قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211858/%d8%ad%d8%b3%db%8c%d9%86%db%8c-%da%a9%d9%87-%d8%af%d8%b1-%d9%85%db%8c%d8%a7%d9%86-%d9%85%d8%a7%d8%b3%d8%aa/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/fd33f405d82b0bea3afb6f60fae88e4e712b1ab6_1630239221-e1659989389734-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211858/%d8%ad%d8%b3%db%8c%d9%86%db%8c-%da%a9%d9%87-%d8%af%d8%b1-%d9%85%db%8c%d8%a7%d9%86-%d9%85%d8%a7%d8%b3%d8%aa/" rel="bookmark">حسینی که در میان ماست</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/mhmd_hadi_shraii/" title="">محمد هادی صحرایی </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>2 روز قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211855/%d9%85%d9%84%d8%aa-%d8%a7%d9%85%d8%a7%d9%85-%d8%ad%d8%b3%db%8c%d9%86%d8%b9%d9%84%db%8c%d9%87-%d8%a7%d9%84%d8%b3%d9%84%d8%a7%d9%85%d8%b3%d9%86%da%af%e2%80%8c%d8%aa%d9%85%d8%a7%d9%85-%da%af%d8%b0/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/n00045327-b-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211855/%d9%85%d9%84%d8%aa-%d8%a7%d9%85%d8%a7%d9%85-%d8%ad%d8%b3%db%8c%d9%86%d8%b9%d9%84%db%8c%d9%87-%d8%a7%d9%84%d8%b3%d9%84%d8%a7%d9%85%d8%b3%d9%86%da%af%e2%80%8c%d8%aa%d9%85%d8%a7%d9%85-%da%af%d8%b0/" rel="bookmark">ملت امام حسین(علیه السلام)سنگ‌تمام گذاشت</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/arash_86/" title="">آرش </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>2 روز قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a></span>
	
</p>
					
					</li>
																		<li class="other-news tie_audio">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211816/%d8%ac%d9%84%d8%b3%d9%87-%d8%b4%d8%a8-%d9%86%d9%87%d9%85-%d9%85%d8%ad%d8%b1%d9%85-%d8%a7%d9%84%d8%ad%d8%b1%d8%a7%d9%85-%d8%b3%d8%ae%d9%86%d8%b1%d8%a7%d9%86%db%8c-%d8%ad%d8%ac%d8%aa-%d8%a7%d9%84%d8%a7/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/IMG_۰۲۰۶۲۰۲۲_۲۲۰۶۱۷_600_x_400_pixel-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211816/%d8%ac%d9%84%d8%b3%d9%87-%d8%b4%d8%a8-%d9%86%d9%87%d9%85-%d9%85%d8%ad%d8%b1%d9%85-%d8%a7%d9%84%d8%ad%d8%b1%d8%a7%d9%85-%d8%b3%d8%ae%d9%86%d8%b1%d8%a7%d9%86%db%8c-%d8%ad%d8%ac%d8%aa-%d8%a7%d9%84%d8%a7/" rel="bookmark">جلسه شب نهم محرم الحرام: سخنرانی حجت الاسلام سیدمهدی سجادی</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/43_seyed-mehdi-sajjadi/" title="">حجت الاسلام سید مهدی سجادی </a></span>
	
<span class="tie-date"><i class="fa fa-clock-o"></i>2 روز قبل</span>	<span class="post-cats"><i class="fa fa-folder"></i><a href="http://serateshgh.com/category/serateshgh/%d9%85%d8%b9%d8%b1%d9%81%d8%aa/%d8%b4%d9%88%d8%b1%d8%a7%db%8c-%d9%86%d9%88%db%8c%d8%b3%d9%86%d8%af%da%af%d8%a7%d9%86/" rel="category tag">شورای نویسندگان</a>, <a href="http://serateshgh.com/category/serateshgh/" rel="category tag">صراط عشق</a>, <a href="http://serateshgh.com/category/serateshgh/%d8%b5%d9%88%d8%aa/%d9%82%d8%b1%d8%a2%d9%86-%da%a9%d8%b1%db%8c%d9%85/" rel="category tag">قرآن کریم</a></span>
	
</p>
					
					</li>
																		<li class="other-news">
									
							<div class="post-thumbnail">
								<a href="http://serateshgh.com/211849/%d8%b9%d8%b2%d8%a7%d8%af%d8%a7%d8%b1%db%8c-%d8%b9%d8%a7%d8%b4%d9%88%d8%b1%d8%a7-%d8%af%d8%b1-%da%a9%d8%b4%d9%85%db%8c%d8%b1/" rel="bookmark"><img width="110" height="75" src="http://serateshgh.com/farsi/wp-content/uploads/2022/08/14010517001028637955824382603654_49801_PhotoX-1-110x75.jpg" class="attachment-tie-small size-tie-small wp-post-image" alt="" /><span class="fa overlay-icon"></span></a>
							</div><!-- post-thumbnail /-->
									
						<h3 class="post-box-title"><a href="http://serateshgh.com/211849/%d8%b9%d8%b2%d8%a7%d8%af%d8%a7%d8%b1%db%8c-%d8%b9%d8%a7%d8%b4%d9%88%d8%b1%d8%a7-%d8%af%d8%b1-%da%a9%d8%b4%d9%85%db%8c%d8%b1/" rel="bookmark">عزاداری عاشورا در کشمیر</a></h3>
						<p class="post-meta">
		
	<span class="post-meta-author"><i class="fa fa-user"></i><a href="http://serateshgh.com/author/hamsayeh_36/" title="">همسایه </a></span>

    """

titles = []
urls = []

soup = BeautifulSoup (source,'html.parser')
other_news = soup.find_all('li',attrs={'class':'other-news'})

for i in range(len(other_news)):


    persian_title = re.findall("mark\">(.+?)</a></h3>",str(other_news[i]))
    # if "\u200c" in persian_title[0]:
    #     persian_title[0] = str(persian_title[0]).replace("\u200c",' ')
    titles.append(persian_title[0])
    # print(persian_title)
    url = re.findall("href=\"(.+?)\"",str(other_news[i]))
    urls.append(url[0])
    # print(url)



df = pd.DataFrame({"titles" : titles , "urls": urls})
writer = pd.ExcelWriter("serate_eshg_news.xlsx")
df.to_excel(writer,"sheet1")
writer.save()
