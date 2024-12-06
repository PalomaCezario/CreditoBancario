import dash
import plotly.graph_objects as go
import pandas as pd
from dash import Dash, dcc, html

# Criando a aplicação Dash
app = Dash(__name__)

# Dados simulados para os gráficos (substitua isso pelos dados reais de sua aplicação)
data_approval_time = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
    'August', 'September', 'October', 'November', 'December'],
    'Average Approval Time (days)': [10, 15, 8, 12, 14, 13, 10, 11, 9, 14, 12, 13]
}
df_approval_time = pd.DataFrame(data_approval_time)

data_distribution_value = {
    'Loan Value': [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000],
    'Count': [15, 20, 25, 30, 18, 24, 20, 14, 12, 10]
}
df_distribution_value = pd.DataFrame(data_distribution_value)

data_rejection_rate = {
    'Reason': ['Low Credit Score', 'Insufficient Income', 'Incomplete Application', 'High Debt-to-Income', 'Other'],
    'Count': [25, 40, 15, 10, 5]
}
df_rejection_rate = pd.DataFrame(data_rejection_rate)

# Criando o gráfico de barras para o tempo médio de aprovação
fig_approval_time = go.Figure(data=[go.Bar(x=df_approval_time['Month'], y=df_approval_time['Average Approval Time (days)'])])
fig_approval_time.update_layout(title='Average Loan Approval Time', xaxis_title='Month', yaxis_title='Time (days)')

# Criando o histograma para a distribuição de empréstimos por valor solicitado
fig_distribution_value = go.Figure(data=[go.Bar(x=df_distribution_value['Loan Value'], y=df_distribution_value['Count'])])
fig_distribution_value.update_layout(title='Distribution of Loans by Requested Amount', xaxis_title='Loan Value', yaxis_title='Count')

# Criando o gráfico de barras horizontais para a taxa de rejeição por motivo
fig_rejection_rate = go.Figure(data=[go.Bar(
    x=df_rejection_rate['Count'], 
    y=df_rejection_rate['Reason'], 
    orientation='h'
)])
fig_rejection_rate.update_layout(title='Rejection Rate by Reason', xaxis_title='Count', yaxis_title='Reason')

# Layout da aplicação Dash com gráficos exibidos um abaixo do outro
app.layout = html.Div([
  
  html.H1(
    'Loan Analysis Dashboard', 
    style={
        'textAlign': 'center',  # Corrigido para o formato correto
        'marginBottom': '20px',
        'color': 'white',  # Cor branca
        'fontFamily': 'Arial, sans-serif',  # Fonte estilizada
        'fontWeight': 'bold',  # Peso da fonte
        'fontSize': '36px'  # Tamanho da fonte
    }
),

    # Gráfico 1: Tempo médio de aprovação
    html.Div([
        dcc.Graph(figure=fig_approval_time, id='graph1'),
    ], style={'margin-bottom': '40px'}),

    html.Hr(),  # Separador entre gráficos

    # Gráfico 2: Distribuição dos empréstimos
    html.Div([
        dcc.Graph(figure=fig_distribution_value, id='graph2'),
    ], style={'margin-bottom': '40px'}),

    html.Hr(),  # Separador entre gráficos

    # Gráfico 3: Taxa de rejeição por motivo
    html.Div([
        dcc.Graph(figure=fig_rejection_rate, id='graph3'),
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
