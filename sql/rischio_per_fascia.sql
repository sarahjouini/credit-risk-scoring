SELECT
    rischio_finale,
    COUNT(*) AS numero_aziende
FROM aziende
GROUP BY rischio_finale
ORDER BY numero_aziende DESC;