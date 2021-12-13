<h2>Data Warehouse: CSV flat files -> Python -> Tableau -> Server -> Business Analysis -> New data</h2>
<h3>Intro</h3>
<img src="images/schema.JPG">
<h3>Data Warehousing consists of following steps:</h3>
<ol>
  <li>CSV as dasta extracts from different systems,</li>
  <li>Python for ETL (extract, transform, load),</li>
  <li>Tableau for data visualization dasboards,</li>
  <li>Server to get dasboard published for stakeholders,</li>
  <li>Busines Analysis,</li>
  <li>New data coming in from systems to storage,</li>
  <li>Go to step 1.</li>
</ol>
<h3>Demo with conclusions</h3>
<ul>
  <li>Python script combines flat files into one Tableau input.</li>
  <li>In this case I use static source  which is CSV flat files <b>(batch processing)</b>.</li>
  <li>However data pipelines are built also for real-time sources where target system requires constant data update <b>(stream processing)</b>.</li>
  <li>The example shows that ultimate destination of data pipelines doesn't have to be a data warehouse.</li>
  <li>Data pipeline can route the processed data into another applications like Tableu for building dashboards.</li>
  <li>Once dashboard built, there is the Tableau option for sending it into server.</li>
  <li>Once published, we can perfrom Business Analysis</li>
  <li>Making decisions based on BA leads to process improvements</li>
  <li>Process improvements generates new data that can undergo the Data Warehousing process all over again.</li>
  <li>Data Warehouse is a great tool for monitoring business processes and continuous improvement impementation.</li>
</ul>

<h3>Tableau Dashboard</h3>
<img src="images/dashboard.JPG">
<br>
<br>
<img src="images/dashboard2.JPG">
<h3>Business Analysis</h3>
<ul>
  <li>Taking conclusions from the analysis that can improve business perfomance.</li>
  <li>Conclusions based on the Tableau dashboard (data generated randomnly so the analysis is purely hypothetic):</li>
    <ul>
      <li>Only one country has positive cashflow as opposed to other countries. That means clients form Italy pay the money into their accounts.</li>
      <li>...</li>
    </ul>
<ul>
  
  
  
  Example: Create Context Filters
This example walks you through how to create a context filter. First you’ll filter a view to show the top 10 products by sales. Then you’ll create a context filter on product category so you can see the top 10 furniture products.

Use the Sample - Superstore data source to create the initial view shown below. The view shows the sales for all sub-categories, sorted with the highest sale at the top.



Now create a Top 10 filter to just show the top selling products. You can create this filter by dragging the Sub-Category field to the Filters shelf. In the Filter dialog box, switch to the Top tab and define a filter that is Top 10 by Sum of Sales. See Filter Data from Your Views(Link opens in a new window) to learn more about defining a Top N filter.



When you click OK, you’ll see that the view is filtered to show the top 10 product sub-categories in terms of sales.



Now, let’s add another filter to show only furniture products. Drag the Category field to the Filters shelf and select only Furniture. When finished, click OK.

The view is filtered but instead of 10 products, it now shows 3. This is because by default all filters are evaluated separately and the view shows the intersection of the results. So this view shows that three of the top 10 overall products are furniture products.



To find out what the top 10 furniture products are we need to make the Category filter a context filter. Right-click the field on the Filters shelf and select Add to Context.

The filter is marked as a context filter and the view updates to show the top four furniture products. Why not 10? Because only four of the sub-categories contain furniture. But we now know that the Top 10 filter is being evaluated on the results of that context.


