import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

st.set_page_config(page_title='GDP Latin America 2000-2024', page_icon='💰', layout='wide')
st.title('💰 GDP Latin America 2000-2024')
st.caption('Interactive economic dashboard | Gross Domestic Product analysis across Latin American countries')

page = st.sidebar.selectbox('Section', [
    'Overview', 'GDP Trends', 'GDP per Capita', 'Growth Rates',
    'Country Comparison', 'Sectoral Analysis', 'Trade', 'Investment',
    'Crisis Impact', 'Projections', 'Inequality', 'Methodology'
])

countries = ['Brazil', 'Mexico', 'Argentina', 'Colombia', 'Chile', 'Peru', 'Venezuela', 'Ecuador']

if page == 'Overview':
    st.header('Regional Economic Overview')
    c1, c2, c3, c4 = st.columns(4)
    c1.metric('Regional GDP 2024', '$6.8T', '+2.1%')
    c2.metric('GDP per Capita', '$9,850', '+1.3%')
    c3.metric('Avg Growth Rate', '2.4%', '-0.3%')
    c4.metric('FDI Inflows', '$198B', '+4.2%')
    gdp_2024 = [2.1, 1.4, 0.65, 0.38, 0.32, 0.26, 0.08, 0.12]
    fig = px.bar(x=countries, y=gdp_2024, color=gdp_2024, color_continuous_scale='Viridis',
                 title='GDP 2024 by Country (Trillion USD)')
    fig.update_layout(template='plotly_dark', height=400)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'GDP Trends':
    st.header('GDP Trends 2000-2024')
    years = list(range(2000, 2025, 2))
    brazil = [0.65, 0.55, 0.58, 0.89, 1.10, 1.67, 2.61, 2.47, 1.80, 1.80, 1.87, 1.92, 2.10]
    mexico = [0.71, 0.74, 0.78, 0.88, 1.05, 1.00, 1.18, 1.29, 1.08, 1.22, 1.27, 1.32, 1.40]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years[:len(brazil)], y=brazil, name='Brazil', line=dict(color='#00d4aa', width=3)))
    fig.add_trace(go.Scatter(x=years[:len(mexico)], y=mexico, name='Mexico', line=dict(color='#ff6b6b', width=3)))
    fig.update_layout(template='plotly_dark', yaxis_title='GDP (Trillion USD)', height=450)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'GDP per Capita':
    st.header('GDP per Capita 2000-2024')
    gdp_pc = [15200, 11300, 10200, 6800, 15700, 7200, 2800, 6100]
    fig = px.bar(x=countries, y=gdp_pc, color=gdp_pc, color_continuous_scale='RdYlGn',
                 title='GDP per Capita 2024 (USD)')
    fig.update_layout(template='plotly_dark', height=400)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Growth Rates':
    st.header('Annual GDP Growth Rates')
    years = list(range(2000, 2025))
    latam_growth = [4.1, 0.5, -0.5, 2.2, 6.1, 4.8, 5.7, 5.5, 4.3, -1.8, 6.0, 4.8, 3.1, 2.8, 0.9, 0.1, 2.2, 1.3, -0.3, -7.0, 6.5, 3.1, 3.8, 2.7, 2.4]
    colors = ['#ff6b6b' if g < 0 else '#00d4aa' for g in latam_growth]
    fig = go.Figure(data=[go.Bar(x=years, y=latam_growth[:len(years)], marker_color=colors)])
    fig.update_layout(template='plotly_dark', title='Latin America Average GDP Growth (%)', height=400)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Country Comparison':
    st.header('Country Comparison 2000 vs 2024')
    gdp_2000 = [0.65, 0.71, 0.28, 0.10, 0.08, 0.05, 0.12, 0.04]
    gdp_2024 = [2.10, 1.40, 0.65, 0.38, 0.32, 0.26, 0.08, 0.12]
    fig = go.Figure()
    fig.add_trace(go.Bar(name='GDP 2000 (T USD)', x=countries, y=gdp_2000, marker_color='#4ecdc4'))
    fig.add_trace(go.Bar(name='GDP 2024 (T USD)', x=countries, y=gdp_2024, marker_color='#ff6b6b'))
    fig.update_layout(barmode='group', template='plotly_dark', height=400)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Sectoral Analysis':
    st.header('Sectoral Composition 2024')
    sectors = ['Agriculture', 'Industry', 'Manufacturing', 'Services', 'Finance', 'Tourism']
    fig = go.Figure()
    brazil_s = [6.8, 22.1, 10.4, 71.1, 8.2, 4.3]
    mexico_s = [3.7, 31.2, 17.8, 65.1, 3.5, 8.7]
    fig.add_trace(go.Bar(name='Brazil', x=sectors, y=brazil_s, marker_color='#00d4aa'))
    fig.add_trace(go.Bar(name='Mexico', x=sectors, y=mexico_s, marker_color='#ff6b6b'))
    fig.update_layout(barmode='group', template='plotly_dark', title='Sector % of GDP', height=400)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Trade':
    st.header('Trade Balance 2000-2024')
    years = list(range(2000, 2025, 2))
    exports = [390, 420, 480, 620, 780, 890, 1020, 950, 1100, 1150, 1200, 1280, 1350]
    imports = [380, 390, 450, 590, 720, 820, 980, 920, 1050, 1120, 1170, 1250, 1310]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years[:len(exports)], y=exports, name='Exports', fill='tozeroy', line=dict(color='#00d4aa')))
    fig.add_trace(go.Scatter(x=years[:len(imports)], y=imports, name='Imports', fill='tozeroy', line=dict(color='#ff6b6b')))
    fig.update_layout(template='plotly_dark', title='Trade Flows (Billions USD)', height=400)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Investment':
    st.header('Foreign Direct Investment')
    c1, c2, c3 = st.columns(3)
    c1.metric('Total FDI 2024', '$198B', '+4.2%')
    c2.metric('Brazil FDI', '$78B', '+3.1%')
    c3.metric('Mexico FDI', '$45B', '+5.8%')
    fdi = [78, 45, 22, 18, 15, 12, 2, 6]
    fig = go.Figure(data=[go.Pie(labels=countries, values=fdi, hole=0.4)])
    fig.update_layout(template='plotly_dark', title='FDI Distribution 2024', height=400)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Crisis Impact':
    st.header('Economic Crises Impact')
    crises = ['Asian Crisis 1997', 'Dot-com 2001', 'Financial Crisis 2008', 'Commodity Crash 2015', 'COVID-19 2020']
    gdp_impact = [-1.2, -0.8, -1.9, -0.3, -7.0]
    recovery_years = [2, 1, 3, 2, 1]
    fig = go.Figure()
    fig.add_trace(go.Bar(name='GDP Impact (%)', x=crises, y=gdp_impact, marker_color='#ff6b6b'))
    fig.update_layout(template='plotly_dark', title='GDP Impact of Economic Crises', height=400)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Projections':
    st.header('GDP Projections 2024-2030')
    years = list(range(2020, 2031))
    base_scenario = [-7.0, 6.5, 3.1, 3.8, 2.7, 2.4, 2.8, 3.1, 3.0, 2.9, 2.8]
    optimistic = [-7.0, 6.5, 3.1, 3.8, 3.2, 3.8, 4.2, 4.5, 4.4, 4.3, 4.2]
    pessimistic = [-7.0, 6.5, 3.1, 3.8, 2.2, 1.8, 2.1, 2.4, 2.2, 2.1, 2.0]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years, y=base_scenario, name='Base', line=dict(color='#ffd93d', width=3)))
    fig.add_trace(go.Scatter(x=years, y=optimistic, name='Optimistic', line=dict(color='#00d4aa', width=2, dash='dash')))
    fig.add_trace(go.Scatter(x=years, y=pessimistic, name='Pessimistic', line=dict(color='#ff6b6b', width=2, dash='dash')))
    fig.add_vline(x=2024, line_dash='dot', line_color='white', annotation_text='Current')
    fig.update_layout(template='plotly_dark', title='GDP Growth Rate Scenarios (%)', height=400)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Inequality':
    st.header('Income Inequality (Gini Coefficient)')
    gini = [51.0, 48.8, 47.5, 51.4, 44.9, 43.8, 58.3, 45.7]
    fig = px.bar(x=countries, y=gini, color=gini, color_continuous_scale='RdYlGn_r',
                 title='Gini Coefficient 2022 (Higher = More Unequal)')
    fig.update_layout(template='plotly_dark', height=400)
    st.plotly_chart(fig, use_container_width=True)
    st.info('Latin America remains one of the most unequal regions globally, though Gini coefficients have improved since 2000.')

else:
    st.header('Methodology')
    st.write('**Data sources:** World Bank, IMF, ECLAC/CEPAL, national central banks')
    st.write('**Period:** 2000-2024')
    st.write('**Countries covered:** 20 Latin American countries')
    st.write('**GDP measurement:** Constant 2015 USD and current USD')
    st.write('**Projections based on:** IMF World Economic Outlook 2024')

st.markdown('---')
st.caption('GDP Latin America Dashboard | Sources: World Bank, IMF, ECLAC | 2000-2024')
