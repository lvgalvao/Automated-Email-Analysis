from loguru import logger
import pandas as pd

# Configura o logger, já existe post sobre ele no meu perfil
logger.remove()
logger.add("./logs/analysis_results.txt", format="{message}")

def analysis():
    df = pd.read_csv('./data/dataset.csv')

    # 1. Análises usando pandas, você pode substituir pelas suas análises
    logger.info(f"Média de Temperatura: {round(df['Temperature'].mean(), 2)}")
    logger.info(f"Média de Pressão: {round(df['Pressure'].mean(), 2)}")
    logger.info(f"Média de Vibração: {round(df['Vibration'].mean(), 2)}")

    # 2. Número de máquinas que precisam de manutenção
    machines_needing_maintenance = df[df['Maintenance_Required'] == 'Yes'].shape[0]
    logger.info(f"Número de máquinas que precisam de manutenção: {machines_needing_maintenance}")

    # 3. Máquinas com necessidade de manutenção
    operators_with_issues = df[df['Maintenance_Required'] == 'Yes']['Machine_ID'].unique()
    logger.info(f"Máquinas que precisam de manutenção: {operators_with_issues}")

if __name__ == "__main__":
    analysis()
