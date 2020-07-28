function view_plot(value)
{
    switch(value)
    {
        case 'plot1': plot('./json/plot1.json', '(Plot-1)');break;
        case 'plot2': plot('./json/plot2.json', '(Plot-2)');break;
        case 'plot3': plot('./json/plot3.json', '(Plot-3)');break;
        case 'plot4': plot('./json/plot4.json', '(Plot-4)');break;
    }
}

function plot(path, plot_number)
{
    fetch(path).then(response=>response.json()).then(
        data=>
          {
            Highcharts.chart('container', {
            chart: {
              type: 'column'
            },
            title: {
              text: data['title'],
              style:{fontSize:'30px',color:'darkred',fontWeight:'bold',textDecoration:'underline'}
            },
            subtitle: {
                text: plot_number,
                style:{fontSize:'15px',color:'blue',fontWeight:'bold'}
              },
            xAxis: {
              title: {
                text: data['x_axis_title'],
                style:{fontSize:'15px',color:'darkred',fontWeight:'bold'}
              },
              labels: {
                style: {
                  fontSize: "14px",
                  fontWeight:'bold',
                  color:'maroon'
                }
              },
              categories: data['x_axis_points'],
              crosshair: true 
            },
            yAxis: {
              min: 0,
              title: {
                text: data['y_axis_title'],
                style:{fontSize:'15px',color:'darkred',fontWeight:'bold'}
              },
              labels: {
                style: {
                  fontSize: "14px",
                  fontWeight:'bold',
                  color:'maroon'
                }
              }
            },
            tooltip: {
                headerFormat: '<span style="font-weight:bold;font-size:13px;">{point.key}</span><table>',
                pointFormat: '<tr><td style="font-size:16px;font-weight:bold;color:{series.color};padding:0">{series.name}: </td>' +
                  '<td style="padding:0"><b>{point.y:.0f} people</b></td></tr>',
                footerFormat: '</table>',
                shared: true,  
                useHTML: true  
              },
            plotOptions: {
              column: {
                pointPadding: 0.2,
                borderWidth: 0 
              }
            },
            series: data['plot_data']
          })
        });    
}
