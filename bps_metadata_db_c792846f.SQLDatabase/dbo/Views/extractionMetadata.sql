CREATE   VIEW [dbo].[extractionMetadata] AS
SELECT 
    vm.[SystemName],
    sd.[sourceType],
    vm.[CDSViewName],
    vm.[Context],
    vm.[Description],
    vm.[Type],
    vm.[ODPName],
    vm.[Delta],
    vm.[KeyFields],
    vm.[relatedCDSViewName],
    es.[isEnabled] AS IsTableEnabled,
    esd.[isEnabled] AS IsDatasetEnabled,
    CASE 
        WHEN es.[isEnabled] = 1 AND esd.[isEnabled] = 1 THEN 1 
        ELSE 0 
    END AS inScope
FROM dbo.viewMetadata vm
JOIN dbo.extractionScope es 
    ON es.TableName = vm.CDSViewName 
   AND es.SystemName = vm.SystemName
JOIN dbo.extractionScopeByDataset esd 
    ON es.DatasetName = esd.DatasetName 
   AND es.SystemName = esd.SystemName
JOIN dbo.SystemDetails sd 
    ON sd.SystemName = vm.SystemName;

GO

