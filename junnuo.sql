CREATE TABLE IF NOT EXISTS `invitations`(
   `invitation_id` VARCHAR(100) NOT NULL,
   `guest_name` VARCHAR(100) NOT NULL,
   `invitation_time` VARCHAR(40) NOT NULL,
   `main_lawyer_name` VARCHAR(40) NOT NULL,
   `assistant_name` VARCHAR(40) NOT NULL,
   `contact_number` VARCHAR(40) NOT NULL,
   `guest_count` INT,
   PRIMARY KEY ( `invitation_id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO invitations
(invitation_id,guest_name,invitation_time,main_lawyer_name,assistant_name,contact_number,guest_count)
VALUES
('invitation_lc','余紫清','2023-01-08','龙成','小何','13524586524',4);

ALTER TABLE invitations
ADD COLUMN invitation_hour INT NOT NULL;